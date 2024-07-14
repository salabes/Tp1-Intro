from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Jugadores(db.model):
    __tablename__ = 'jugadores'
    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'))
    posicion_id = db.Column(db.Integer, db.ForeignKey('posiciones.id'))
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicaciones.id'))
    nombre = db.Column(db.String[255], nullable=False)
    apellido = db.Column(db.String[255], nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    pie = db.Column(db.String[255], nullable=False)

class Equipos(db.model):
    __tablename__ = 'equipos'
    id = db.Column(db.Integer, primary_key=True)
    formacion_id = db.Column(db.Integer, db.ForeignKey('formaciones.id'))
    nombre = db.Column(db.String[255], nullable=False)

class Formaciones(db.model):
    __tablename__ = 'formaciones'
    id = db.Column(db.Integer, primary_key=True)
    tipo_formacion_id = db.Column(db.Integer, db.ForeignKey('tipo_formaciones.id'))

class Tipo_Formaciones(db.model):
    __tablename__ = 'tipo_formaciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String[255], nullable=False)

class Posiciones(db.model):
    __tablename__ = 'posiciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String[255], nullable=False)

class Ubicaciones(db.model):
    __tablename__ = 'ubicaciones'
    id = db.Column(db.Integer, primary_key=True)
    posicion_id = db.Column(db.Integer, db.ForeignKey('posiciones.id'))
    tipo_formacion_id = db.Column(db.Integer, db.ForeignKey('tipo_formaciones.id'))
    lugar_en_la_formacion = db.Column(db.Integer, nullable=False)