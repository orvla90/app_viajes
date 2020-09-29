from app import db


class Datos_viajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), index=True, unique=False)
    personas = db.relationship('Datos_personas', backref='lista_personas', lazy='dynamic', cascade = "all, delete, delete-orphan")
    gastos = db.relationship('Datos_gastos', backref='lista_gastos', lazy='dynamic', cascade = "all, delete, delete-orphan")

    def __repr__(self):
        return '{id} | {nombre}'.format(id=self.id, nombre=self.nombre)


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
