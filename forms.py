from wtforms import  Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField, TextAreaField, PasswordField, RadioField
from wtforms import validators

def my_validation(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError("El campo NO tiene datos")


class Userform(Form):
    matricula = StringField('Matricula', 
        [validators.DataRequired(message = 'El campo Matrícula es requerido'),
         validators.length(min=5, max=10, message = 'Ingresa mínimo 5 y máximo 10')])
    nombre = StringField('Nombre', 
        [validators.DataRequired(message = 'El campo Nombre es requerido')])
    apaterno = StringField('Apaterno')
    amarterno = StringField('Amaterno')
    email = EmailField('Correo')

class LoginForm(Form):
    username = StringField('Usuario', 
        [validators.DataRequired(message = 'El campo Usuario es requerido'),
         validators.length(min = 5, max = 10, message = 'Ingresa min 5, max 10')])
    
    password = StringField('Contraseña', 
        [validators.DataRequired(message = 'El campo Contraseña es requerido'),
         validators.length(min = 5, max = 10, message = 'Ingresa min 5, max 10')])