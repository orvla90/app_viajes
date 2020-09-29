from flask import Flask, render_template, redirect, url_for, request
from viajes import viajes
from forms import Viaje, Persona, Gasto
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecretKey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///viajes.db'

db = SQLAlchemy(app)


import routes