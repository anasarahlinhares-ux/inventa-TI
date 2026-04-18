from flask import Flask, render_template
from controllers.auth_controller import auth_bp
from models.user import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['SECRET_KEY'] = 'segredo'

db.init_app(app)

app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()

    if not User.query.filter_by(email="admin@email.com").first():
        user = User(email="admin@email.com", password="1234")
        db.session.add(user)
        db.session.commit()

    if __name__ == "__main__":
        app.run(debug=True)


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/equipamentos")
def equipamentos():
    return render_template("total_de_equipamentos.html")

@app.route("/lista")
def lista():
    return render_template("lista_de_equipamentos.html")

@app.route("/notebook")
def notebook():
    return render_template("icone_notebook.html")

@app.route("/samsung")
def samsung():
    return render_template("icone_samsung.html")


if __name__ == "__main__":
    app.run(debug=True)
