from flask import Flask, request, jsonify
from models import db, Jugador, Equipo, Formacion, TipoFormacion, Posicion

app = Flask(__name__)
port = 5000

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/ligaargentina'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=port, debug=True)


