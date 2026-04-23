from flask import Flask
from models import db, User, Post, Comment, Media

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def hello():
    return "¡Servidor Flask funcionando correctamente!"

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5000)