from wtforms import  Form
from wtforms import IntegerField, StringField
from wtforms.fields import FieldList

class CajaForm(Form):
    numeros = FieldList(StringField('numeros'), min_entries=1)
