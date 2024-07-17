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
                'formacion_id': equipo.formacion_id,
                'nombre': equipo.nombre,
                'escudo': equipo.escudo
            }
            equipos_data.append(equipo_data)
        return jsonify(equipos_data)
    except:
        return jsonify({'mensaje': 'No hay equipos'}), 500

@app.route('/equipo/<id_equipo>', methods=['GET'])
def get_equipo(id_equipo):
    try:
        equipo = Equipo.query.get(id_equipo)
        if not equipo:
            return jsonify({'mensaje': 'Equipo no encontrado'}), 404
        
        equipo_data = {
            'id': equipo.id,
            'formacion_id': equipo.formacion_id,
            'nombre': equipo.nombre,
            'escudo': equipo.escudo
        }
        return jsonify(equipo_data), 200
    except:
        return jsonify({'mensaje': 'Error al obtener el equipo'}), 500

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=port, debug=True)
