from flask import Flask, request, jsonify
from models import db, Jugadores, Equipos, Formaciones, Tipo_Formaciones, Posiciones

app = Flask(__name__)
port = 5000

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://user:password@localhost:5432/basedededatos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=port, debug=True)


