from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, length, NumberRange, Regexp
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, DecimalField, EmailField

class UserFrom(Form):
    matricula=StringField("Matricula")
    edad=IntegerField("Edad")
    nombre=StringField("Nombre")
    apellidos=StringField("Apellidos")
    email=EmailField("Correo")