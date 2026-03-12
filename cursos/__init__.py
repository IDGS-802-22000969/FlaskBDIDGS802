from flask import Blueprint
from .routes import cursos
cursos = Blueprint(
    'cursos',
    __name__,
    template_folder='templates')