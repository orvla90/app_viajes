from flask import Flask, render_template


viajes = Flask(__name__)

@viajes.route('/')
def index():

    return(render_template('index.html'))