from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(FlaskForm):
    id = IntegerField('Id', [
        validators.Optional()
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=50, message="Ingrese un valor válido")])
    
    apaterno = StringField('Apaterno', [
        validators.DataRequired(message="El campo es requerido")])
    
    email = EmailField('Email', [
        validators.DataRequired(message="El campo es requerido")])
    
    telefono = EmailField('Telefono', [
        validators.DataRequired(message="El campo es requerido")])