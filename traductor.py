from wtforms import  Form, StringField, validators

class traductor(Form):
    espanol = StringField('Español', [validators.DataRequired(message="El campo es requerido"), 
                                      validators.length(min=1)])
    ingles = StringField('Inglés', [validators.DataRequired(message="El campo es requerido"), 
                                      validators.length(min=1)])
    
class diccionario(Form):
    palabra = StringField('Palabra')



