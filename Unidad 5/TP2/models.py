from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy(app)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    DNI = db.Column(db.Integer, nullable = False, unique = True)
    Clave = db.Column(db.String(120), nullable = False)
    Tipo = db.Column(db.String(8), nullable = False)
    pedido = db.relationship('Pedidos', backref = 'usuarios', cascade="all, delete-orphan", lazy='dynamic')

class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    NumPedido = db.Column(db.Integer)
    Fecha = db.Column(db.DateTime)
    Total = db.Column(db.Float)
    Cobrado = db.Column(db.Boolean)
    Observacion = db.Column(db.String(80), nullable = False)
    DNIMozo = db.Column(db.Integer, db.ForeignKey('usuarios.DNI'), nullable = False)
    Mesa = db.Column(db.Integer, nullable = False)
    item = db.relationship('ItemsPedidos', backref = 'itemspedidos', cascade = "all, delete-orphan", lazy = 'dynamic')

class ItemsPedidos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    NumItem = db.Column(db.Integer, unique = True)
    NumPedido = db.Column(db.Integer, db.ForeignKey('pedidos.NumPedido'))
    NumProducto = db.Column(db.Integer, db.ForeignKey('productos.NumProducto'))
    Precio = db.column(db.Integer, db.ForeignKey('productos.PrecioUnitario'))
    Estado = db.column(db.String(30))

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    NumProducto = db.Column(db.Integer, nullable = False, unique = True)
    Nombre = db.Column(db.String(120), nullable = False)
    PrecioUnitario = db.Column(db.Float, nullable = False)
    item = db.relationship('ItemsPedidos', backref = 'itemspedidos', cascade = "all, delete-orphan", lazy = 'dynamic')