from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime, ForeignKey, func
from app import db

class Comentario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fecha = db.Column(DateTime, default=func.now())
	contenido = db.Column(db.Text)
	usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))    
    
	def __init__(self, contenido, usuario_id):        
		self.contenido = contenido		
		self.usuario_id = usuario_id