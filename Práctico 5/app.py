from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from user import Login, Logout  #inicia sesión, cierra sesión
from pprint import pprint
import hashlib

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Usuario, Viaje, Movil

# redirige a la página para iniciar sesión o registrarse en la app
@app.route('/')
def inicioregistro():
    return render_template('inicioregistro.html')

# redirige a la página para registrarse en la app
@app.route('/Registrarse')
def registro():
    return render_template('registro.html')

# realiza el registro de un usuario
@app.route('/RegistradoExitosamente', methods = ['POST', 'GET'])
def registroexitoso():
    if request.method == 'POST':
        dni = request.form['dni']
        if dni.isdigit() != True:
            return render_template('error.html', error = 'ERROR: El DNI va escrito sólo en números.', band = 'Registro')
        nom = request.form['name']
        if nom.isalpha() != True:
            nombre = nom.split()
            if nombre[0].isalpha() != True:
                return render_template('error.html', error = 'ERROR: El nombre se escribe solo con letras.', band = 'Registro')
            elif nombre[1].isalpha() != True:
                return render_template('error.html', error = 'ERROR: El nombre se escribe solo con letras.', band = 'Registro')
        conEncriptada = hashlib.md5(bytes(request.form['password'], encoding='utf-8'))
        cla = conEncriptada.hexdigest()
        tip = request.form['tipo']
        usuario = Usuario(DNI = dni, Nombre = nom, Clave = cla, Tipo = tip)
        db.session.add(usuario)
        db.session.commit()
        mensaje = 'Registrado con éxito!'
        if usuario.Tipo == 'Operario':
            Login(usuario)
            return render_template('vistaOperario.html', msj = mensaje)
        elif usuario.Tipo == 'Cliente':
            Login(usuario)
            return render_template('vistaCliente.html', msj = mensaje)
        else:
            return render_template('error.html', error = 'ERROR: El tipo de usuario no coincide con los registrados.')
    else:
        return render_template('registro.html')

# redirige a la página para iniciar sesión en la app
@app.route('/Iniciar Sesion')
def inicio():
    return render_template('inicio.html')

# redirige a la página de inicio del operario
@app.route('/VistaOperario')
def vistaoperario():
    return render_template('vistaOperario.html')

# redirige a la página de inicio del cliente
@app.route('/VistaCliente')
def vistacliente():
    return render_template('vistaCliente.html')

# verifica el usuario para iniciar sesión
@app.route('/Aplicacion', methods = ['POST', 'GET'])
def aplicacion():
    if request.method == 'POST':
        if not request.form['dni'] or not request.form['password']:
            return render_template('error.html', error = 'Por favor ingrese los datos requeridos.')
        else:
            if (request.form['dni']).isdigit() != True:
                return render_template('error.html', error = 'ERROR: El DNI va escrito sólo en números.')
            else:
                usuario_actual = Usuario.query.filter_by(DNI = request.form['dni']).first()
                if usuario_actual is None:
                    return render_template('error.html', error = 'ERROR: El DNI no esta registrado.')
                else:
                    conEncriptada = hashlib.md5(bytes(request.form['password'], encoding='utf-8'))
                    clave = conEncriptada.hexdigest()
                    if usuario_actual.Clave == clave:
                        if usuario_actual.Tipo == 'Operario':
                            Login(usuario_actual)
                            return render_template('vistaOperario.html')
                        elif usuario_actual.Tipo == 'Cliente':
                            Login(usuario_actual)
                            return render_template('vistaCliente.html')
                        else:
                            return render_template('error.html', error = 'ERROR: El tipo de usuario no coincide con los registrados.')
                    else:
                        return render_template('error.html', error = 'ERROR: La contraseña no es valida.')
    else:
        return render_template('inicio.html')

# redirige a la página para solicitar un móvil
@app.route('/Solicitudparaunmóvil', methods = ['POST', 'GET'])
def solicitamovil():
    return render_template('solicitarmovil.html')

# un cliente registra la solicitud de un móvil
@app.route('/RegistrarSolicitud', methods = ['POST', 'GET'])
def registrarsolicitud():
    if request.method == 'POST':
        if request.form['personas'].isdigit() == True:
            listadeviajes = Viaje.query.all()
            cantidaddeviajes = len(listadeviajes) - 1
            numerodeviaje = int(listadeviajes[cantidaddeviajes].IdViaje) + 1
            f = datetime.now()
            fecha = datetime.strftime(f, '%Y-%m-%d')
            importe = 0 # sin calcular 
            origen = request.form['origen']
            destino = request.form['destino']
            #cantidad = request.form['personas']
            #equipaje = request.form['equipaje']
            numeromovil = 0 #sin asignar por el operador
            demora = 0 #sin asignar por el operador
            duracion = 0 #sin asignar por el operador
            viaje = Viaje(IdViaje = numerodeviaje, Origen = origen, Destino = destino, Fecha = fecha, Demora = demora, Duracion = duracion, Importe = importe, DniCliente = session['DNI'], NumMovil = numeromovil)
            db.session.add(viaje)
            db.session.commit()
            mensaje = 'Móvil solicitado con éxito!'
            return render_template('vistaCliente.html', msj = mensaje)
        else:
            return render_template('error.html', error = 'ERROR: Ingresar la cantidad de personas en números.')

# un cliente consulta los móviles que tenga pendiente
@app.route('/ConsultarMovil', methods = ['POST', 'GET'])
@app.route('/ConsultarMovil/<int:ID>', methods = ['POST', 'GET'])
def consultarmovil(ID = 0):
    if ID == 0:
        listadeviajes = Viaje.query.all()
        return render_template('consultarmovil.html', viajes = listadeviajes, band = 0)
    else:
        listadeviajes = Viaje.query.all()
        listademoviles = Movil.query.all()
        viaj = Viaje.query.filter_by(IdViaje = ID).first()
        return render_template('consultarmovil.html', viajes = listadeviajes, moviles = listademoviles, viaje = viaj, band = 1)

# un operario asigna un móvil a un viaje
@app.route('/AsignarMovil', methods = ['POST', 'GET'])
@app.route('/AsignarMovil/<int:ID>', methods = ['POST', 'GET'])
def asignarmovil(ID = 0):
    if ID == 0:
        listadeviajes = Viaje.query.all()
        listademoviles = Movil.query.all()
        return render_template('asignarmovil.html', viajes = listadeviajes, moviles = listademoviles, band = 0)
    else:
        listadeviajes = Viaje.query.all()
        listademoviles = Movil.query.all()
        viaj = Viaje.query.filter_by(IdViaje = ID).first()
        return render_template('asignarmovil.html', viajes = listadeviajes, moviles = listademoviles, band = 1, viaje = viaj)

# confirma la asignación de un móvil a un viaje
@app.route('/ConfirmarAsignacionDeMovil/<int:ID>', methods = ['POST', 'GET'])
def confirmarasignaciondemovil(ID = 0):
    listademoviles = Movil.query.all()
    viaje = Viaje.query.filter_by(IdViaje = ID).first()
    db.session.delete(viaje)
    demora = request.form['espera']
    nummovil = request.form['movil']
    i = 0
    band = False
    while i < len(listademoviles):
        if listademoviles[i].Numero == nummovil:
            i = len(listademoviles)
            band = True
        i += 1
    if not band:
        return render_template('error.html', error = 'ERROR: El número de móvil ingresado es incorrecto.')
    nuevoviaje = Viaje(IdViaje = ID, Origen = viaje.Origen, Destino = viaje.Destino, Fecha = viaje.Fecha, Demora = demora, Duracion = viaje.Duracion, Importe = viaje.Importe, DniCliente = viaje.DniCliente, NumMovil = nummovil)
    db.session.add(nuevoviaje)
    db.session.commit()
    listadeviajes = Viaje.query.all()
    return render_template('asignarmovil.html', viajes = listadeviajes, moviles = listademoviles, band = 0)

# un operario finaliza viajes
@app.route('/FinalizarViaje', methods = ['POST', 'GET'])
@app.route('/FinalizarViaje/<int:ID>', methods = ['POST', 'GET'])
def finalizarviaje(ID = 0):
    if ID == 0:
        listadeviajes = Viaje.query.all()
        return render_template('finalizarviaje.html', viajes = listadeviajes, cantidadviajes = len(listadeviajes),band = 0)
    else:
        listadeviajes = Viaje.query.all()
        viaj = Viaje.query.filter_by(IdViaje = ID).first()
        return render_template('finalizarviaje.html', viajes = listadeviajes, cantidadviajes = len(listadeviajes),viaje = viaj, band = 1)

# se confirma la finalización del viaje
@app.route('/ConfirmarFinalizacionDelViaje/<int:ID>', methods = ['POST', 'GET'])
def confirmarfinalizaciondelviaje(ID = 0):
    viaje = Viaje.query.filter_by(IdViaje = ID).first()
    db.session.delete(viaje)
    duracion = int(request.form['duracion'])
    importebase = 100
    importevariable = (duracion * 5)
    importedelviaje = importebase + importevariable
    if int(viaje.Demora) > 15:
        p = (10 * importedelviaje) / 100
        importedelviaje -= p
    nuevoviaje = Viaje(IdViaje = ID, Origen = viaje.Origen, Destino = viaje.Destino, Fecha = viaje.Fecha, Demora = viaje.Demora, Duracion = duracion, Importe = importedelviaje, DniCliente = viaje.DniCliente, NumMovil = viaje.NumMovil)
    db.session.add(nuevoviaje)
    db.session.commit()
    listadeviajes = Viaje.query.all()
    return render_template('finalizarviaje.html', viajes = listadeviajes, cantidadviajes = len(listadeviajes),band = 0)

# un operario consulta los viajes realizados en una fecha por movil
@app.route('/ConsultarViajesRealizados', methods = ['POST', 'GET'])
@app.route('/ConsultarViajesRealizados/<int:ID>', methods = ['POST', 'GET'])
def consultarviajesrealizados(ID = 0):
    if ID == 0:
        listademoviles = Movil.query.all()
        return render_template('consultarviajesrealizados.html', moviles = listademoviles, band = 0)
    else:
        listademoviles = Movil.query.all()
        listadeviajes = Viaje.query.all()
        i = 0
        nummovil = request.form['movil']
        date = str(request.form['fecha'])
        while i < len(listademoviles):
            if str(nummovil) == str(listademoviles[i].Numero):
                mov = listademoviles[i]
                i = len(listademoviles)
            i += 1
        sinviajess = True
        for viaje in listadeviajes:
            if str(viaje.NumMovil) == str(mov.Numero):
                sinviajess = False
        return render_template('consultarviajesrealizados.html', moviles = listademoviles, viajes = listadeviajes, movil = mov, band = 1, sinviajes = sinviajess, fecha = date)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

# funcion para cerrar sesión
@app.route('/logout')
def logout():
    Logout()
    return redirect(url_for('inicioregistro'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)