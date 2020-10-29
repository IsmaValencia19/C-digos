from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, prymary_key = True)
    type = db.Column(db.String(8), nullable = False)
    name = db.Column(db.String(80), nullable = False)
    user = db.Column(db.String(8), unique = True, nullable = False)
    key = db.Column(db.String(120), nullable = False)

class Pedido(db.Model):
    id = db.Column(db.Integer, prymary_key = True)
    table_number = db.Column(db.Integer, nullable = False)
    waiters_name = db.Column(db.String(80), nullable = False)
    items = db.relationship('Item', backref = 'pedido', cascade = 'all, delete-orphan', lazy = 'dynamic')
    price = db.Column(db.Float, nullable = False)

class Item(db.Model):
    id = db.Column(db.Integer, prymary_key = True)
    name = db.Column(db.String(120), nullable = False)
    state = db.Column(db.Boolean, nullable = False)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(20), nullable = False)
    name = db.Column(db.String(120), nullable = False)
    unit_price = db.Column(db.Float, nullable = False)