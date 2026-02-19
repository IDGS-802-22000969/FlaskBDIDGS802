from wtforms import FloatField, Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators
from wtforms import RadioField

class UserForm(Form):
    id = IntegerField('ID', [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1000, max= 100000000, message="Ingrese un valor valido")])
    
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max= 50, message="Ingrese un valor valido")])
    
    apaterno = StringField('Apaterno', [
        validators.DataRequired(message="El campo es requerido")])
    
    amaterno= StringField('Amaterno', [
        validators.DataRequired(message="El campo es requerido")])
    
    correo = StringField('Correo', [
        validators.DataRequired(message="El campo es requerido")])

