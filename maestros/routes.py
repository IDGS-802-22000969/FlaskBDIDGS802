from flask import Blueprint, render_template, request, redirect, url_for
import forms
from models import db, Maestros

maestros = Blueprint('maestros', __name__)

@maestros.route("/maestroTabla")
def maestroTabla():
    lista_maestros = Maestros.query.all()
    return render_template("maestro_tabla.html", maestros=lista_maestros)

@maestros.route("/maestroNuevo", methods=['GET', 'POST'])
def maestroNuevo():
    form = forms.MaestroForm(request.form)

    if request.method == 'POST' and form.validate():
        maestro = Maestros(
            matricula=form.matricula.data,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            especialidad=form.especialidad.data,
            email=form.email.data
        )
        db.session.add(maestro)
        db.session.commit()

        return redirect(url_for('maestros.maestroTabla'))
    return render_template("maestros.html", form=form)

@maestros.route("/maestrosDetalles")
def maestrosDetalles():
    matricula = int(request.args.get('matricula'))
    maestro = Maestros.query.get(matricula)

    return render_template("detalles_maestro.html", maestro=maestro)


@maestros.route("/maestrosModificar", methods=['GET', 'POST'])
def maestrosModificar():
    matricula = int(request.args.get('matricula'))
    maestro = Maestros.query.get(matricula)
    form = forms.MaestroForm(request.form, obj=maestro)
    if request.method == 'POST' and form.validate():
        maestro.nombre = form.nombre.data
        maestro.apellidos = form.apellidos.data
        maestro.especialidad = form.especialidad.data
        maestro.email = form.email.data

        db.session.commit()
        return redirect(url_for('maestros.maestroTabla'))
    return render_template("modificar_maestro.html", form=form, maestro=maestro)

@maestros.route("/maestrosEliminar")
def maestrosEliminar():
    matricula = int(request.args.get('matricula'))
    maestro = Maestros.query.get(matricula)

    db.session.delete(maestro)
    db.session.commit()

    return redirect(url_for('maestros.maestroTabla'))