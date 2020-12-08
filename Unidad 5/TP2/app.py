from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Usuarios, Pedidos, Productos, ItemsPedidos

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/Aplicacion', methods = ['POST', 'GET'])
def aplicacion():
    if request.method == 'POST':
        if not request.form['dni'] or not request.form['password']:
            return render_template('error.html', error = 'Por favor ingrese los datos requeridos.')
        else:
            usuario_actual = Usuarios.query.filter_by(DNI = request.form['dni']).first()
            if usuario_actual is None:
                return render_template('error.html', error = 'El DNI no esta registrado.')
            else:
                if usuario_actual.Clave == request.form['password']:
                    if usuario_actual.Tipo == 'Mozo':
                        return render_template('vistaMozo.html', datos = usuario_actual)
                    elif usuario_actual.Tipo == 'Cocinero':
                        return render_template('vistaCocinero.html', datos = usuario_actual)
                    else:
                        return render_template('error.html', error = 'ERROR DE TIPO, no coincide con los registrados.')
                else:
                    return render_template('error.html', error = 'La contraseña no es valida.')
    else:
        return render_template('inicio.html')

@app.route('/RegistrarPedido', methods = ['POST', 'GET'])
def registrarPedido():
    pass

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)