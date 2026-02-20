from typing import Required

from wtforms import form
from wtforms.validators import email

from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms

from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf=CSRFProtect()

app = Flask(__name__)

@app.route("/Alumnos", methods=['GET', 'POST'])
def Alunos():
	create_form=forms.UserForm(request.form)
	if request.method=='POST':
		alum=Alumnos(nombre=create_form.nombre.data,
			   apaterno=create_form.apaterno.data,
			   email=create_form.email.data)
		db.session.add(alum)
		db.sessiom.commit()
		return redirect(url_for('index'))
	
	return render_template("alumnos.html", form=create_form)


@app.errorhandler(404)
def pag_not_fount(e):
	return render_template("404.html"), 404
	

@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index():
	create_form=forms.UserForm(request.form)
	alumno=Alumnos.query.all()
	return render_template("index.html", form=create_form, alumno=alumno)

@app.route("/detalles", methods=['GET', 'POST'])
def Alunos():
	create_from=forms.UserForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).firs()
		id=request.args.get('id')
		nombre=alum1.nombre
		apaterno=alum1.apaterno
		email=alum1.email
	return render_template("detalles.html", nombre=nombre, apaterno=apaterno, email=email)


@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
	create_from=forms.UserForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alum1=db.session.query(Alumnos).filter(Alumnos.id==id).firs()
		create_from.id.data=request.args.get('id')
		create_from.nombre=alum1.nombre
		create_from.apaterno=alum1.apaterno
		create_from.email=alum1.email
	if request.methods=='POST':
		id=alum_class.id.data
		alumn=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alumn.id=id
		alumn.nombre=str.rstrip(alumno_class.nombre.data)
		alumn.apaterno=alumno_class.apaterno.data
		alumn.email=alumno_class.email.data
		db.session.add(alumn)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("modificar.html", form=alumno_class)



if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
app.run()
	