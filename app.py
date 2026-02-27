from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from models import db, Alumnos
from maestros import maestros
from maestros.routes import maestros
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)

db.init_app(app)
migrate=Migrate(app, db)
csrf = CSRFProtect(app)

@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index():
    form = forms.UserForm()
    alumnos = Alumnos.query.all()
    return render_template("index.html", alumnos=alumnos, form=form)

@app.route("/alumnoTabla")
def alumnoTabla():
    alumnos = Alumnos.query.all()
    return render_template("index.html", alumnos=alumnos)

@app.route("/Alumnos", methods=['GET', 'POST'])
def alumno():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST' and create_form.validate():
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit() 
        return redirect(url_for('index'))
    
    return render_template("alumnos.html", form=create_form)

@app.route('/detalles', methods=['GET', 'POST'])
def detalles():
    alumno_class = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alumn1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alumn1:
            nombre = alumn1.nombre
            apaterno = alumn1.apaterno
            email = alumn1.email
            telefono = alumn1.telefono
    return render_template("detalles.html", nombre=nombre, apaterno=apaterno, email=email, telefono=telefono)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
    id = request.args.get('id')
    alum1 = Alumnos.query.get_or_404(id)
    create_form = forms.UserForm(request.form, obj=alum1)
    if request.method == 'POST' and create_form.validate():
        alum1.nombre = create_form.nombre.data
        alum1.apaterno = create_form.apaterno.data
        alum1.email = create_form.email.data
        
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('index'))
        
    return render_template("modificar.html", form=create_form)


@app.route("/eliminar", methods=['GET', 'POST']) 
def eliminar():
    id = request.args.get('id')
    alum1 = Alumnos.query.get_or_404(id)
    
    if request.method == 'POST':
        db.session.delete(alum1)
        db.session.commit()
        return redirect(url_for('index'))
        
    create_form = forms.UserForm(obj=alum1)
    return render_template("eliminar.html", form=create_form, alumno=alum1)

@app.errorhandler(404)
def pag_not_found(e): 
    return render_template("404.html"), 404

if __name__== '__main__':
    with app.app_context():
        db.create_all()
    app.run()