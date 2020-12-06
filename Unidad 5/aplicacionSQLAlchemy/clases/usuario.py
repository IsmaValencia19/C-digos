from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from app import db

class Usuario(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(80), nullable=False)
	correo = db.Column(db.String(120), unique=True, nullable=False)
	clave = db.Column(db.String(120), nullable=False)    
	comentario = db.relationship('Comentario', backref='usuario', cascade="all, delete-orphan" , lazy='dynamic')
    
	def __init__(self, nombre, correo, clave):
		self.nombre = nombre
		self.correo = correo
		self.clave = clave