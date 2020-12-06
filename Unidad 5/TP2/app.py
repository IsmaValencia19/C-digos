from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Usuarios, Pedidos, Productos, ItemsPedidos

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/bienvenida', methods = ['POST', 'GET'])
def bienvenida():
    if request.method == 'POST':
        if not request.form['dni'] or not request.form['password']:
            return render_template('error.html', error = 'Por favor ingrese los datos requeridos.')
        else:
            usuario_actual = Usuarios.query.filter_by(dni = request.form['dni']).first()
            if usuario_actual is None:
                return render_template('error.html', error = 'El DNI no esta registrado.')
            else:
                verificacion = check_password_hash(usuario_actual.Clave, request.form['password'])
                if (verificacion):
                    return render_template('bienvenida.html', usuario_actual)
                else:
                    return render_template('error.html', error = 'La contraseña no es valida.')
    else:
        return render_template('inicio.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)