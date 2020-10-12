from flask import Flask, render_template, redirect, url_for, request
from models import Datos_viajes, Datos_personas, Datos_gastos
from app import app, db
from forms import Viaje, Persona, Gasto
from sqlalchemy import and_
from utils import calcular_movimientos, calcular_lista_deudas
from flask_login import current_user, login_user, logout_user, login_required


# index
@app.route('/')
def index():
    return(render_template('index.html', viajes=Datos_viajes.query.all()))

# Viajes

# carga lista de viajes
@app.route('/viaje/<int:id_viaje>')
@login_required
def web_viaje(id_viaje):
    datos_personas = Datos_personas()
    viaje = Datos_viajes().query.filter_by(id=id_viaje).first()
    personas = datos_personas.query.filter_by(id_viaje=id_viaje).all()
    gastos = Datos_gastos.query.filter_by(id_viaje=id_viaje).all()
    return(render_template('viaje.html', personas=personas, viaje=viaje, gastos=gastos))



# añade un nuevo viaje
@app.route('/nuevo_viaje', methods = ['GET', 'POST'])
@login_required
def nuevo_viaje():
    viaje = Viaje()
    if viaje.validate_on_submit():
        nuevo_viaje = Datos_viajes(nombre = viaje.nombre_viaje.data)
        db.session.add(nuevo_viaje)
        db.session.commit()
        return(redirect(url_for('index')))
    return(render_template('nuevo_viaje.html', viaje=viaje))

# Personas

# Añade una persona nueva
@app.route('/nueva_persona/<int:id_viaje>', methods = ['GET', 'POST'])
@login_required
def nueva_persona(id_viaje):
    persona = Persona()
    if persona.validate_on_submit():
        nueva_persona = persona.nombre_persona.data
        baremo = persona.baremo_persona.data
        db.session.add(Datos_personas(nombre=nueva_persona, baremo=baremo, cantidad_pagada=0.0, coste_viaje=0.0, id_viaje=id_viaje))
        db.session.commit()
        return(redirect(url_for('index')))
    return(render_template('nueva_persona.html', persona=persona))

# Gastos

# carga todos los gastos
@app.route('/gastos/<int:id_viaje>')
@login_required
def web_gastos(id_viaje):
    gastos = Datos_gastos().query.filter_by(id_viaje=id_viaje).all()
    return(render_template('gastos.html', gastos=gastos))

# Añade un gasto nuevo
@app.route('/nuevo_gasto/<int:id_viaje>', methods = ['GET', 'POST'])
@login_required
def nuevo_gasto(id_viaje):
    if len(Datos_personas().query.filter_by(id_viaje=id_viaje).all()) < 1:
        return(redirect(url_for('web_viaje', id_viaje=id_viaje)))
    gasto = Gasto()
    personas = Datos_personas().query.filter_by(id_viaje=id_viaje).all()
    nombre_personas = [persona.nombre for persona in personas]
    id_personas = [persona.id for persona in personas]
    gasto.persona_paga.choices = nombre_personas
    gasto.personas_participan.choices = zip(id_personas, personas)
    if gasto.validate_on_submit():
        nombre_gasto = gasto.nombre_gasto.data
        cantidad = gasto.pagado.data
        persona_paga = gasto.persona_paga.data
        # añade el gasto que ha pagado la persona 
        Datos_personas().query.filter(and_(Datos_personas.nombre==persona_paga, Datos_personas.id_viaje==id_viaje)).first().cantidad_pagada += cantidad
        personas_participan = gasto.personas_participan.data
        # añadir la cantida al coste del viaje a cada persona que participa
        baremo_total = 0
        for persona in personas_participan:
            baremo_total += Datos_personas().query.filter_by(id=persona).first().baremo
        for persona in personas_participan:
            datos_persona = Datos_personas().query.filter_by(id=persona).first()
            datos_persona.coste_viaje += cantidad/baremo_total * datos_persona.baremo
        personas_participan = [str(persona) for persona in personas_participan]
        nuevo_gasto = Datos_gastos(nombre=nombre_gasto, cantidad=cantidad, persona_paga=persona_paga, personas_participan=' '.join(personas_participan), id_viaje=id_viaje)
        db.session.add(nuevo_gasto)
        db.session.commit()
        return(redirect(url_for('index')))
    return(render_template('nuevo_gasto.html', gasto=gasto, personas=personas))

#calcula los pagos que tiene que hacer cada persona
@app.route('/movimientos/<int:id_viaje>')
@login_required
def movimientos(id_viaje):
    personas = Datos_personas().query.filter_by(id_viaje=id_viaje).all()
    lista_deudas = calcular_lista_deudas(personas)
    return(calcular_movimientos(lista_deudas))

# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
      return(redirect(url_for('index')))
    #crear Formulario para login
    return('')

# register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return(redirect(url_for('index')))
    # crear Formulario de registro