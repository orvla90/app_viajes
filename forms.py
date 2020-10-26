from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectMultipleField, SelectField, FloatField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


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

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')