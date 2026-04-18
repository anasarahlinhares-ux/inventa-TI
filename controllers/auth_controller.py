from flask import Blueprint, render_template, request, redirect, url_for
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login")
def login():
    return render_template("login.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def process_login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    user = User.query.filter_by(email=email).first()

    if user and user.password == senha:
        return redirect(url_for("auth.dashboard"))
    else:
        return "login invalido"

@auth_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@auth_bp.route("/equipamentos")
def equipamentos():
    return render_template("total_de_equipamentos.html")

@auth_bp.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@auth_bp.route("/lista")
def lista():
    return render_template("lista_de_equipamentos.html")

@auth_bp.route("/notebook")
def notebook():
    return render_template("icone_notebook.html")

@auth_bp.route("/samsung")
def samsung():
    return render_template("icone_samsung.html")

