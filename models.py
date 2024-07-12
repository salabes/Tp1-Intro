import dateline
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Jugadores(db.model):
    __tablename__ = 'jugadores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String[255], nullable=false)
    apellido = db.Column(db.String[255], nullable=false)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'))
    posicion_id = db.Column(db.Integer, db.ForeignKey('posiciones.id'))
    edad = db.Column(db.Integer, nullable=false)
    pie = db.Column(db.String[255], nullable=false)

class Equipos(db.model):
    __tablename__ = 'equipos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String[255], nullable=false)

class Formaciones(db.model):
    __tablename__ = 'formaciones'
    id = db.Column(db.Integer, primary_key=True)
    tipo_formaciones_id = db.Column(db.Integer, db.ForeignKey('tipo_formaciones.id'))
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'))

class Tipo_Formaciones(db.model):
    __tablename__ = 'formaciones'
    id = db.Column(db.Integer, primary_key=True)

class Posiciones(db.model):
    __tablename__ = 'posiciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String[255], nullable=false)


