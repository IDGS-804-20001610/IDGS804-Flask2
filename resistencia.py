from wtforms import  Form, StringField, SelectField, RadioField, validators

class ResForm(Form):
    colore2 = [("", "---"), (0, 'NEGRO'), (1, 'CAFE'), (2, 'ROJO'), (3, 'NARANJA'), (4, 'AMARILLO'),
               (5, 'VERDE'), (6, 'AZUL'), (7, 'MORADO'), (8, 'GRIS'), (9, 'BLANCO')]
    
    colore3 = [("", "---"), (1, 'NEGRO'), (10, 'CAFE'), (100, 'ROJO'), (1000, 'NARANJA'), (10000, 'AMARILLO'),
               (10000, 'VERDE'), (100000, 'AZUL'), (1000000, 'MORADO'), (10000000, 'GRIS'), (100000000, 'BLANCO')]

    colo1 = [(0.05, 'ORO'), (0.1, 'PLATA')]

    banda1 = SelectField('Banda 1', [validators.DataRequired(message = "SELECCIONE UN COLOR")], coerce = str, choices = colore2)
    banda2 = SelectField('Banda 2', [validators.DataRequired(message = "SELECCIONE UN COLOR")], coerce = str, choices = colore2)
    banda3 = SelectField('Banda 3', [validators.DataRequired(message = "SELECCIONE UN COLOR")], coerce = str, choices = colore3)

    tolerancia = RadioField('Tolerancia', [validators.DataRequired(message = "SELECCIONE UN COLOR")], coerce = str, choices = colo1)
