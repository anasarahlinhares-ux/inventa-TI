from flask import Flask, render_template, jsonify
from controllers.auth_controller import auth_bp
from models.user import User
from models.equipamento import Equipamento
from models import db
import os

app = Flask(__name__)

app.json.ensure_ascii = False

# Configurações
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'segredo'

db.init_app(app)

with app.app_context():
    db.create_all()

    if not User.query.filter_by(email="admin@email.com").first():
        user = User(email="admin@email.com", password="1234")
        db.session.add(user)
        db.session.commit()

# 🔥 SÓ REGISTRA O BLUEPRINT
app.register_blueprint(auth_bp)

# 🔥 SOMENTE ESSAS ROTAS AQUI (que não estão no blueprint)
@app.route("/")
def index():
    return render_template("login.html")

    if not User.query.filter_by(email="admin@email.com").first():
        user = User(email="admin@email.com", password="1234")
        db.session.add(user)
        db.session.commit()

@app.route("/autor")
def autor():
    return jsonify({
        "nome": "Ana Sarah Anastacio Linhares",
        "curso": "Técnico em Informática para Internet",
        "disciplina": "Desenvolvimento Web II",
        "projeto": "InventaTI"
    })

@app.route("/api/usuarios")
def api_usuarios():
    usuarios = User.query.all()

    return jsonify([
        {
            "id": usuario.id,
            "email": usuario.email
        }
        for usuario in usuarios
    ])


if __name__ == "__main__":
    app.run(debug=True)
