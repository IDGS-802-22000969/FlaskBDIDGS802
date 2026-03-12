from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Cursos, Alumnos
from forms import InscripcionForm

inscripciones = Blueprint('inscripciones', __name__)

@inscripciones.route("/inscripcionesTabla")
def inscripcionesTabla():
    lista_cursos = Cursos.query.all()
    return render_template("inscripciones_tabla.html", cursos=lista_cursos)

@inscripciones.route("/inscripcionDetalles")
def inscripcionDetalles():
    id_alumno = request.args.get('alumno_id')
    id_curso = request.args.get('curso_id')
    alumno = Alumnos.query.get_or_404(id_alumno)
    curso = Cursos.query.get_or_404(id_curso)
    return render_template("inscripcion_detalles.html", alumno=alumno, curso=curso)

@inscripciones.route("/inscripcionNueva", methods=["GET", "POST"])
def inscripcionNueva():
    if request.method == "POST":
        id_curso = request.form.get("curso_id")
        id_alumno = request.form.get("alumno_id")
        curso = Cursos.query.get(id_curso)
        alumno = Alumnos.query.get(id_alumno)
        if curso and alumno:
            try:
                curso.alumnos.append(alumno)
                db.session.commit()
                return redirect(url_for('cursos.cursoDetalles', id=id_curso))
            except Exception as e:
                db.session.rollback()
                return "Error: El alumno ya está inscrito en este curso."
    lista_alumnos = Alumnos.query.all()
    lista_cursos = Cursos.query.all()
    return render_template("inscripcion_nueva.html", alumnos=lista_alumnos, cursos=lista_cursos)

@inscripciones.route("/inscripcionModificar", methods=["GET", "POST"])
def inscripcionModificar():
    id_al = request.args.get('alumno_id')
    id_cur = request.args.get('curso_id')
    alumno = Alumnos.query.get_or_404(id_al)
    curso_actual = Cursos.query.get_or_404(id_cur)

    if request.method == "POST":
        nuevo_id_curso = request.form.get("nuevo_curso_id")
        nuevo_curso = Cursos.query.get(nuevo_id_curso)
        if alumno in nuevo_curso.alumnos:
            return "Error: El alumno ya está inscrito en ese curso."
        curso_actual.alumnos.remove(alumno)
        nuevo_curso.alumnos.append(alumno)
        db.session.commit()
        return redirect(url_for('inscripciones.inscripcionesTabla'))
    cursos = Cursos.query.all()
    return render_template("inscripcion_modificar.html", alumno=alumno, curso_actual=curso_actual, cursos=cursos)

@inscripciones.route("/inscripcionEliminar", methods=["GET", "POST"])
def inscripcionEliminar():
    id_alumno = request.args.get('alumno_id')
    id_curso = request.args.get('curso_id')
    alumno = Alumnos.query.get_or_404(id_alumno)
    curso = Cursos.query.get_or_404(id_curso)
    form = InscripcionForm()
    if request.method == "POST":
        curso.alumnos.remove(alumno)
        db.session.commit()
        return redirect(url_for('inscripciones.inscripcionesTabla'))

    return render_template("inscripcion_eliminar.html", alumno=alumno, curso=curso, form=form)