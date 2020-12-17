from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pprint import pprint

import hashlib

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Usuarios, Pedidos, Productos, ItemsPedidos

listaPedidosEliminados = []
listaNOM=[]
listaPRE=[]

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/Aplicacion', methods = ['POST', 'GET'])
def aplicacion():
    if request.method == 'POST':
        if not request.form['dni'] or not request.form['password']:
            return render_template('error.html', error = 'Por favor ingrese los datos requeridos.')
        else:
            if (request.form['dni']).isdigit() != True:
                return render_template('error.html', error = 'Ingrese en el DNI solo números.')
            else:
                usuario_actual = Usuarios.query.filter_by(DNI = request.form['dni']).first()
                if usuario_actual is None:
                    return render_template('error.html', error = 'El DNI no esta registrado.')
                else:
                    conEncriptada = hashlib.md5(bytes(request.form['password'], encoding='utf-8'))
                    clave = conEncriptada.hexdigest()
                    if usuario_actual.Clave == clave:
                        if usuario_actual.Tipo == 'Mozo':
                            return render_template('vistaMozo.html')
                        elif usuario_actual.Tipo == 'Cocinero':
                            return render_template('vistaCocinero.html', datos = usuario_actual)
                        else:
                            return render_template('error.html', error = 'ERROR DE TIPO, no coincide con los registrados.')
                    else:
                        return render_template('error.html', error = 'La contraseña no es valida.')
    else:
        return render_template('inicio.html')

@app.route('/Mesa')
def mesa():
    return render_template('Mesa.html')

@app.route('/RegistroPedido', methods = ['POST', 'GET'])
@app.route('/RegistroPedido/<nombre>/<float:precio>/ <int:numMesa>/<int:Pedido>/ <int:numProducto>', methods = ['POST', 'GET'])
def Pedido(nombre = '', precio = 0, numMesa = 0, Pedido = 0, numProducto = 0):
    if nombre == '':
        if request.method == 'POST':
            if (request.form['mesa']).isdigit() == True:
                if request.form['mesa']:
                    mesa = request.form['mesa']
                    pedidos = Pedidos.query.all()
                    cant = len(pedidos)
                    total = 0
                    numpedido = int(pedidos[cant - 1].NumPedido) + 1
                    return render_template('pedido.html', productos = Productos.query.all(), xmesa = mesa, numPedido = numpedido, band = 0, xtotal = total)
            else:
                return render_template('vistaMozo.html', Mensaje = 'La mesa se identifica solamente con números.')
    else:
        listaNOM.append(nombre)
        listaPRE.append(precio)
        xband = len(listaPRE)
        total=0
        listaItems = ItemsPedidos.query.all()
        cantitems = len(listaItems)
        xnumItem = int(listaItems[cantitems-1].NumItem) + 1
        Item = ItemsPedidos(NumItem = xnumItem, NumPedido = Pedido, NumProducto = str(numProducto), Precio = precio, Estado = 'Pendiente')
        db.session.add(Item)
        db.session.commit()
        for i in range(len(listaPRE)):
            total += listaPRE[i]
        return render_template('pedido.html', productos = Productos.query.all(), xnombre = listaNOM, xprecio = listaPRE, xmesa = numMesa, numPedido = Pedido, xtotal = total, band = xband)

@app.route('/cargaPedidos/<xnom>/<xpre>/<float:xtot>/<int:xmes>/<int:numPed>/', methods = ['POST', 'GET'])
def cargaPedidos(xnom, xpre, xtot, xmes, numPed):
    if request.method == 'GET':
        usuario_actual = Usuarios.query.filter_by(DNI = '38459309').first()
        pedido = Pedidos(NumPedido = numPed, Fecha = datetime.now(), Total = xtot, Cobrado = 'False', Observacion = request.args.get('observacion'), DNIMozo = usuario_actual.DNI, Mesa = xmes)
        db.session.add(pedido)
        db.session.commit()
        listaNOM[:] = []
        listaPRE[:] = []
        mensaje = 'Pedido registrado con exito!'
        return render_template('vistaMozo.html', Mensaje = mensaje)
    else:
        return render_template('inicio.html')

@app.route('/ConsultaPedidoVigente', methods = ['POST', 'GET'])
def consultaPedidoVigente():
    listaPED = Pedidos.query.all()
    listaITE = ItemsPedidos.query.all()
    cant_pedi = len(listaPED)
    cant_item = len(listaITE)
    return render_template('listadoPedidosVigentes.html', listaPedis = listaPED, listaItems = listaITE, items = cant_item, pedis = cant_pedi)

@app.route('/ConsultaPedidoCobrado', methods = ['POST', 'GET'])
def consultaPedidoCobrado():
    listaPED = Pedidos.query.all()
    listaITE = ItemsPedidos.query.all()
    cant_pedi = len(listaPED)
    cant_item = len(listaITE)
    return render_template('consultarPedidosCobrados.html', listaPedis = listaPED, listaItems = listaITE, items = cant_item, pedis = cant_pedi)

@app.route('/ItemListo', methods = ['POST', 'GET'])
@app.route('/ItemListo/<int:numItem>/<int:numPedi>', methods = ['POST', 'GET'])
def estadoListo(numItem = 0, numPedi = 0):
    if numItem == 0:
        listaPedi = Pedidos.query.all()
        prod = Productos.query.all()
        for pedido in listaPedi:
            contListos = 0
            cantItem = 0
            for item in pedido.item:
                cantItem += 1
                if item.Estado == 'Listo':
                    contListos += 1
            if cantItem == contListos:
                listaPedidosEliminados.append(pedido)
        cantPedList = len(listaPedidosEliminados)
        for i in range(cantPedList):
            listaPedi.remove(listaPedidosEliminados[i-i])
            listaPedidosEliminados.pop(i-i)
        return render_template('indicarItemListo.html', listaPedis = listaPedi, pedis = len(listaPedi), productos = prod, cantProd = len(prod))
    else:
        listaPedi = Pedidos.query.all()
        prod = Productos.query.all()
        valor = listaPedi[numPedi - 2].item[0].NumItem
        ITEM = listaPedi[numPedi - 2].item[numItem - int(valor)]   
        db.session.delete(ITEM)
        Nuevoitem = ItemsPedidos(NumItem = ITEM.NumItem, NumPedido = ITEM.NumPedido, NumProducto = ITEM.NumProducto, Precio = ITEM.Precio, Estado = 'Listo')
        db.session.add(Nuevoitem)
        db.session.commit()
        for pedido in listaPedi:
            contListos = 0
            cantItem = 0
            for item in pedido.item:
                cantItem += 1
                if item.Estado == 'Listo':
                    contListos += 1
            if cantItem == contListos:
                listaPedidosEliminados.append(pedido)
        cantPedList = len(listaPedidosEliminados)
        for i in range(cantPedList):
            listaPedi.remove(listaPedidosEliminados[i-i])
            listaPedidosEliminados.pop(i-i)
        return render_template('indicarItemListo.html', listaPedis = listaPedi, pedis = len(listaPedi), productos = prod, cantProd = len(prod))

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)