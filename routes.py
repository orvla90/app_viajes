from flask import Flask, render_template, redirect, url_for, request
from datos import Datos_viajes, Datos_personas, Datos_gastos
from app import app, db
from forms import Viaje, Persona, Gasto

@app.route('/')
def index():
    return(render_template('index.html', viajes=Datos_viajes.query.all()))


@app.route('/nuevo_viaje', methods = ['GET', 'POST'])
def nuevo_viaje():
    viaje = Viaje()
    if viaje.validate_on_submit():
        nuevo_viaje = Datos_viajes(nombre = viaje.nombre_viaje.data)
        db.session.add(nuevo_viaje)
        db.session.commit()
        return(redirect(url_for('index')))
    return(render_template('nuevo_viaje.html', viaje=viaje))

@app.route('/nueva_persona/<int:id_viaje>', methods = ['GET', 'POST'])
def nueva_persona(id_viaje):
    persona = Persona()
    if persona.validate_on_submit():
        nueva_persona = persona.nombre_persona.data
        baremo = persona.baremo_persona.data
        db.session.add(Datos_personas(nombre=nueva_persona, baremo=baremo, cantidad_pagada=0.0, coste_viaje=0.0, id_viaje=id_viaje))
        db.session.commit()
        return(redirect(url_for('index')))
    return(render_template('nueva_persona.html', persona=persona))

@app.route('/nuevo_gasto/<int:id_viaje>', methods = ['GET', 'POST'])
def nuevo_gasto(id_viaje):
    gasto = Gasto()
    if gasto.validate_on_submit():
        nombre_gasto = gasto.nombre_gasto.data
        cantidad = gasto.pagado.data
        persona_paga = gasto.persona_paga.data
        peronas_participan = gasto.personas_participan.data
        viajes[id_viaje]['gastos'].append({'nombre':nombre_gasto, 'cantidad': cantidad, 'persona_paga':persona_paga, 'personas_participan':peronas_participan})
        return(redirect(url_for('index')))
    return(render_template('nuevo_gasto.html', gasto=gasto))