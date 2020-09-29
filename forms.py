from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectMultipleField, SelectField
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
    pagado = IntegerField('Pagado', validators=[DataRequired()])
    #queda hacer query para cambiar las personas por los nombres de las personas que estan en este viaje
    persona_paga = SelectField('Persona que Paga',  choices=['persona1', 'persona2'])
    personas_participan = SelectMultipleField('Personas que Participan', choices=[('1', 'persona1'), ('2', 'persona2')])
    submit = SubmitField('Añadir gasto')