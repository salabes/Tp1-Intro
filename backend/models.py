import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Jugadores(db.model):
    __tablename__ = 'jugadores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String[255], nullable=False)
    apellido = db.Column(db.String[255], nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'))
    posicion_id = db.Column(db.Integer, db.ForeignKey('posiciones.id'))
    formacion_id = db.Column(db.Integer, db.ForeignKey('formaciones.id'))
    edad = db.Column(db.Integer, nullable=False)
    pie = db.Column(db.String[255], nullable=False)

class Equipos(db.model):
    __tablename__ = 'equipos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String[255], nullable=False)

class Formaciones(db.model):
    __tablename__ = 'formaciones'
    id = db.Column(db.Integer, primary_key=True)
    tipo_formacion_id = db.Column(db.Integer, db.ForeignKey('tipo_formaciones.id'))
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'))

class Tipo_Formaciones(db.model):
    __tablename__ = 'formaciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String[255], nullable=False)

class Posiciones(db.model):
    __tablename__ = 'posiciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String[255], nullable=False)


