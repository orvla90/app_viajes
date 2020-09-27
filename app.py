from flask import Flask, render_template, redirect, url_for, request
from viajes import viajes
from forms import Viaje, Personas, Gastos

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecretKey'



@app.route('/')
def index():

    return(render_template('index.html', viajes=viajes))

@app.route('/nuevo_viaje', methods = ['GET', 'POST'])
def nuevo_viaje():
    viaje = Viaje()
    if viaje.validate_on_submit():
        nuevo_nombre = viaje.nombre_viaje.data
        viajes[len(viajes)+1] = {'nombre': nuevo_nombre}
        return(redirect(url_for('index')))
    return(render_template('nuevo_viaje.html', viaje = viaje))

@app.route('/nueva_persona/<int:id_viaje>', methods = ['GET', 'POST'])
def nueva_persona(id_viaje):
    persona = Personas(id_viaje)
    if persona.validate_on_submit():
        nueva_persona = persona.nombre_persona.data
        viajes[id_viaje]['personas'].append(nueva_persona) 
        return(redirect(url_for('index')))
    return(render_template('nueva_persona.html', persona=persona))

@app.route('/nuevo_gasto/<int:id_viaje>', methods = ['GET', 'POST'])
def nuevo_gasto(id_viaje):
    gasto = Gastos()
    if gasto.validate_on_submit():
        nombre_gasto = gasto.nombre_gasto.data
        cantidad = gasto.pagado.data
        persona_paga = gasto.persona_paga.data
        peronas_participan = gasto.personas_participan.data
        viajes[id_viaje]['gastos'].append({'nombre':nombre_gasto, 'cantidad': cantidad, 'persona_paga':persona_paga, 'personas_participan':peronas_participan})
        return(redirect(url_for('index')))
    return(render_template('nuevo_gasto.html', gasto=gasto))