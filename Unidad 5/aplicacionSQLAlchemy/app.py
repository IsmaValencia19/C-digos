from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(80), nullable=False)
	correo = db.Column(db.String(120), unique=True, nullable=False)
	clave = db.Column(db.String(120), nullable=False)    
	comentario = db.relationship('Comentario', backref='usuario', cascade="all, delete-orphan", lazy='dynamic')
    
	
class Comentario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fecha = db.Column(db.DateTime)
	contenido = db.Column(db.Text)
	usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))    
	
@app.route('/')
def inicio():
	return render_template('inicio.html')	

@app.route('/nuevo_usuario', methods = ['GET','POST'])
def nuevo_usuario():   
	if request.method == 'POST':
		if not request.form['nombre'] or not request.form['email'] or not request.form['password']:
			return render_template('error.html', error="Los datos ingresados no son correctos...")
		else:
			nuevo_usuario = Usuario(nombre=request.form['nombre'], correo = request.form['email'], clave=request.form['password'])         
			db.session.add(nuevo_usuario)
			db.session.commit()
			flash('El usuario se registró existosamente')
	return render_template('nuevo_usuario.html')
	
@app.route('/listar_usuarios')
def listar_usuarios():
   return render_template('listar_usuarios.html', usuarios = Usuario.query.all())

@app.route('/nuevo_comentario', methods = ['GET','POST'])
def nuevo_comentario():
	if request.method == 'POST':
		if not request.form['password']:
			return render_template('error.html', error="Por favor ingrese su contraseña")
		else:
			usuario_actual= Usuario.query.filter_by(clave=request.form['password']).first()
			if usuario_actual is None:
				return render_template('error.html', error="La contraseña no es válida")
			else:
				return render_template('ingresar_comentario.html', usuario = usuario_actual)
	else:
		return render_template('nuevo_comentario.html')

@app.route('/ingresar_comentario', methods = ['GET', 'POST'])
def ingresar_comentario():
    if request.method == 'POST':
        if not request.form['contenido']:
            return render_template('error.html', error="contenido no ingresado...")
        else:            
            nuevo_comentario= Comentario(fecha=datetime.now(), contenido=request.form['contenido'], usuario_id =request.form['userId'])    
            db.session.add(nuevo_comentario)
            db.session.commit()
            return render_template('inicio.html') 
    return render_template('inicio.html') 

@app.route('/listar_comentarios')
def listar_comentarios():
   return render_template('listar_comentario.html', comentarios = Comentario.query.all())

@app.route('/listar_comentarios_usuario', methods = ['GET', 'POST'])
def listar_comentarios_usuario():  
    if request.method == 'POST':
        if not request.form['usuarios']:
			#Pasa como parámetro todos los usuarios
            return render_template('listar_comentario_usuario.html', usuarios = Usuario.query.all(), usuario_seleccionado = None )
        else:
            return render_template('listar_comentario_usuario.html', usuarios= None, usuario_seleccionado = Usuario.query.get(request.form['usuarios'])) 
    else:
        return render_template('listar_comentario_usuario.html', usuarios = Usuario.query.all(), usuario_seleccionado = None )   
        
@app.route("/comentarios_usuario/<int:usuario_id>")
def comentarios_usuario(usuario_id):
  usuario_seleccionado = Usuario.query.get_or_404(usuario_id)
  return render_template('comentarios_usuario.html', usuario_comentario = usuario_seleccionado.comentario)
  
@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)	
	
#https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application	