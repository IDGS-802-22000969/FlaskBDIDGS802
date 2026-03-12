from flask import Blueprint
from .routes import inscripciones
inscripciones = Blueprint(
    'inscripciones',
    __name__,
    template_folder='templates')