from flask import Blueprint, render_template, request, redirect, url_for
from forms import CursoForm
from models import db, Cursos, Maestros, Alumnos

cursos = Blueprint('cursos', __name__)

@cursos.route("/cursosTabla")
def cursosTabla():
    lista_cursos = Cursos.query.all()
    return render_template("cursos_tabla.html", cursos=lista_cursos)

@cursos.route("/cursoNuevo", methods=["GET", "POST"])
def cursoNuevo():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        maestro_id = request.form.get("maestro_id") 
        nuevo_curso = Cursos(
            nombre=nombre,
            descripcion=descripcion,
            maestro_id=maestro_id
        )   
        db.session.add(nuevo_curso)
        db.session.commit() 
        return redirect(url_for('cursos.cursosTabla'))
    lista_maestros = Maestros.query.all()
    return render_template("curso_nuevo.html", maestros=lista_maestros)

@cursos.route("/cursoDetalles")
def cursoDetalles():
    id_curso = int(request.args.get('id'))
    curso = Cursos.query.get(id_curso)
    return render_template("curso_detalles.html", curso=curso)

@cursos.route("/cursoEliminar", methods=["GET", "POST"])
def cursoEliminar():
    id_curso = request.args.get('id')
    curso = Cursos.query.get_or_404(id_curso)
    form = CursoForm(obj=curso)

    if request.method == "POST":
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for('cursos.cursosTabla'))

    return render_template("curso_eliminar.html", curso=curso, form=form)

@cursos.route("/cursoModificar", methods=["GET", "POST"])
def cursoModificar():
    id_param = request.args.get('id')
    curso = Cursos.query.get_or_404(id_param)
    form = CursoForm(obj=curso) 

    if request.method == "POST":
        curso.nombre = request.form.get("nombre")
        curso.descripcion = request.form.get("descripcion")
        curso.maestro_id = request.form.get("maestro_id")
        db.session.commit()
        return redirect(url_for('cursos.cursosTabla'))

    maestros = Maestros.query.all()
    return render_template("curso_modificar.html", curso=curso, form=form, maestros=maestros)
