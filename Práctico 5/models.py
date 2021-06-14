from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship

db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    DNI = db.Column(db.Integer, primary_key = True, unique = True)
    Nombre = db.Column(db.String(100), nullable = False)
    Clave = db.Column(db.String(120), nullable = False)
    Tipo = db.Column(db.String(30), nullable = False)
    viaje = db.relationship('Viaje', backref = 'usuario')

class Viaje(db.Model):
    __tablename__ = 'Viaje'
    IdViaje = db.Column(db.Integer, primary_key = True, unique = True)
    Origen = db.Column(db.String(200), nullable = False)
    Destino = db.Column(db.String(200), nullable = False)
    Fecha = db.Column(db.String(15))
    Demora = db.Column(db.Integer)
    Duracion = db.Column(db.Integer)
    Importe = db.Column(db.Float)
    DniCliente = db.Column(db.Integer, db.ForeignKey('Usuario.DNI'), nullable = False)
    NumMovil = db.Column(db.Integer, db.ForeignKey('Movil.Numero'))
    Movil = db.relationship('Movil')

class Movil(db.Model):
    __tablename__ = 'Movil'
    Numero = db.Column(db.Integer, primary_key = True, unique = True)
    Patente = db.Column(db.String(10), nullable = False, unique = True)
    Marca = db.Column(db.String(20), nullable = False)
    Viaje = db.relationship('Viaje', backref = 'movil')