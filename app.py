from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from models import db, Alumnos
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


db.init_app(app)
migrate=Migrate(app, db)
csrf = CSRFProtect(app)

@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index():
    form = forms.UserForm()
    alumnos = Alumnos.query.all()
    return render_template("index.html", alumnos=alumnos, form=form)

@app.route("/Alumnos", methods=['GET', 'POST'])
def alumno():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST' and create_form.validate():
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            email=create_form.email.data
        )
        db.session.add(alum)
        db.session.commit() 
        return redirect(url_for('index'))
    
    return render_template("alumnos.html", form=create_form)

@app.route("/detalles", methods=['GET'])
def detalles(): 
    id = request.args.get('id')
    alum1 = Alumnos.query.get_or_404(id)
    return render_template("detalles.html", alumno=alum1)

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

@app.route('/elimin', methods=['GET', 'POST'])
def elimin():
            id = request.args.get('id')
            alum1 = Alumnos.query.get(id)
            create_form = forms.UserForm(request.form, obj=alum1)
            if request.method == 'POST':
                 db.session.delete(alum1)
                 db.session.commit()
            return redirect(url_for('index'))
            create_form = forms.UserForm(obj=alum1)
            return render_template("eliminar.html", form=create_form, alumno=alum1)

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