from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Datos_viajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), index=True, unique=False)
    personas = db.relationship('Datos_personas', backref='lista_personas', lazy='dynamic', cascade = "all, delete, delete-orphan")
    gastos = db.relationship('Datos_gastos', backref='lista_gastos', lazy='dynamic', cascade = "all, delete, delete-orphan")
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return '{nombre}'.format(nombre=self.nombre)


class Datos_personas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), index=True, unique=False)
    baremo = db.Column(db.Integer, index=False, unique=False)
    cantidad_pagada = db.Column(db.Float, index=True, unique=False)
    coste_viaje = db.Column(db.Float, index=False, unique=False)
    id_viaje = db.Column(db.Integer, db.ForeignKey('datos_viajes.id'))
    gastos = db.relationship('Datos_gastos', backref='gastos_personas', lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.nombre)


class Datos_gastos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), index=True, unique=False)
    cantidad = db.Column(db.Float, index=True, unique=False)
    persona_paga = db.Column(db.Integer, db.ForeignKey('datos_personas.id'))
    personas_participan = db.Column(db.String(500), index=True, unique=False)
    id_viaje = db.Column(db.Integer, db.ForeignKey('datos_viajes.id'))

    def __repr__(self):
        return '{nombre} | cantidad: {cantidad}€'.format(nombre=self.nombre, cantidad=self.cantidad)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password = db.Column(db.String(100))
    viajes = db.relationship('Datos_viajes', backref='manager', lazy='dynamic')
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return(check_password_hash(self.password, password))

    def __repr__(self):
        return('<User {name}>'.format(name=self.username))

@login.user_loader
def load_user(id):
    return(User.query.get(int(id)))