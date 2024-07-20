from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Jugador, Equipo, Formacion, Posicion, Ubicacion

app = Flask(__name__)
CORS(app)
port = 5000

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://santiago:Pinchacapo03@localhost:5432/seleccioneshistoricas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/equipos', methods=['GET'])
def get_equipos():
    try:
        equipos = Equipo.query.all()
        equipos_data = []
        for equipo in equipos:
            equipo_data = {
                'id': equipo.id,
                'nombre': equipo.nombre,
                'escudo': equipo.escudo
            }
            equipos_data.append(equipo_data)
        return jsonify(equipos_data)
    except:
        return jsonify({'mensaje': 'No hay equipos'}), 500

@app.route('/equipo/<id_equipo>/formacion', methods=['GET'])
def get_jugadores_en_formacion(id_equipo):
    try:
        jugadores = Jugador.query.filter(
            Jugador.equipo_id == id_equipo,
            Jugador.lugar_en_formacion != None
        ).all()
    
        jugadores_data = []
        for jugador in jugadores:
            jugador_data = {
                'id': jugador.id,
                'equipo_id': jugador.equipo_id,
                'posicion_id': jugador.posicion_id,
                'nombre': jugador.nombre,
                'apellido': jugador.apellido,
                'edad': jugador.edad,
                'pierna_habil': jugador.pierna_habil,
                'lugar_en_formacion': jugador.lugar_en_formacion
            }
            jugadores_data.append(jugador_data)
        return jsonify(jugadores_data)
    except:
        return jsonify({'mensaje': 'No hay jugadores en la formación'}), 500

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=port, debug=True)
