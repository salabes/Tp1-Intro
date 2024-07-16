from flask import Flask, request, jsonify
from models import db, Jugador, Equipo, Formacion, Posicion, Ubicacion

app = Flask(__name__)
port = 5000

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://nicocazal:postgres@localhost:5432/seleccioneshistoricas'
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
                'nombre': equipo.nombre
                'escudo': equipo.escudo
            }
            equipos_data.append(equipo_data)
        return jsonify(equipos_data)
    except:
        return jsonify({'mensaje': 'No hay equipos'}), 500

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=port, debug=True)
