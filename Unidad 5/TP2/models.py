from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy(app)

class Usuarios(db.Model):
    __tablename__ = 'Usuarios'
    DNI = db.Column(db.Integer, primary_key = True, unique = True)
    Clave = db.Column(db.String(120), nullable = False)
    Tipo = db.Column(db.String(10), nullable = False)
    pedido = db.relationship('Pedidos', backref = 'usuarios', cascade="all, delete-orphan", lazy='dynamic')

class Pedidos(db.Model):
    __tablename__ = 'Pedidos'
    NumPedido = db.Column(db.Integer, primary_key = True)
    Fecha = db.Column(db.DateTime)
    Total = db.Column(db.Float)
    Cobrado = db.Column(db.String(20))
    Observacion = db.Column(db.String(80), nullable = False)
    DNIMozo = db.Column(db.Integer, db.ForeignKey('Usuarios.DNI'), nullable = False)
    Mesa = db.Column(db.Integer, nullable = False)
    item = db.relationship('ItemsPedidos', backref = 'itemspedidos', cascade = "all, delete-orphan", lazy = 'dynamic')

class ItemsPedidos(db.Model):
    __tablename__ = 'ItemsPedidos'
    NumItem = db.Column(db.Integer, primary_key = True, unique = True)
    NumPedido = db.Column(db.Integer, db.ForeignKey('Pedidos.NumPedido'))
    NumProducto = db.Column(db.Integer, db.ForeignKey('Productos.NumProducto'))
    Precio = db.Column(db.Float)
    Estado = db.Column(db.String(30))

class Productos(db.Model):
    __tablename__ = 'Productos'
    NumProducto = db.Column(db.Integer, primary_key = True, unique = True)
    Nombre = db.Column(db.String(120), nullable = False)
    PrecioUnitario = db.Column(db.Float, nullable = False)
    item = db.relationship('ItemsPedidos', backref = 'items', cascade = "all, delete-orphan", lazy = 'dynamic')