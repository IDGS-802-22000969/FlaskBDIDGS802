from flask_sqlalchemy import SQLAlchemy

import datatime

db= SQLAlchemy()
class Alumnos(db.Model):
    _tablename_='alumnos'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno = db.Column(db.String(50))
    email=db.Column(db.String(50))
    created_date=db.Colum(db.DateTime,
                    defaul=datatime.datatime.now)
