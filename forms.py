from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectMultipleField, SelectField, FloatField
from wtforms.validators import DataRequired 


class Viaje(FlaskForm):
    nombre_viaje = StringField('Nombre', validators=[DataRequired()])
    submit = SubmitField('Añadir viaje')    

class Persona(FlaskForm):
    nombre_persona = StringField('Nombre', validators=[DataRequired()])
    baremo_persona = IntegerField('Baremo', validators=[DataRequired()])
    submit = SubmitField('Añadir persona')

class Gasto(FlaskForm):
    nombre_gasto = StringField('Nombre', validators=[DataRequired()])
    pagado = FloatField('Pagado', validators=[DataRequired()])
    #queda hacer query para cambiar las personas por los nombres de las personas que estan en este viaje
    persona_paga = SelectField('Persona que Paga', coerce=str)
    personas_participan = SelectMultipleField('Personas que Participan', coerce=int)
    submit = SubmitField('Añadir gasto')