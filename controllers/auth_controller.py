from flask import Blueprint, render_template, request, redirect, url_for
from models.user import User
from models.equipamento import Equipamento
from models import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form.get("email")
    senha = request.form.get("senha")

    user = User.query.filter_by(email=email).first()

    if user and user.password == senha:
        return redirect(url_for("auth.dashboard"))
    else:
        return "login invalido"
    
  return render_template("login.html")

# 🔥 ROTA DO FORMULÁRIO DE CADASTRO (mostra a página)
@auth_bp.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

# 🔥 ROTA PARA SALVAR O EQUIPAMENTO (recebe os dados)
@auth_bp.route("/salvar_equipamento", methods=["POST"])
def salvar_equipamento():
    # PEGA OS VALORES DO FORMULÁRIO
    descricao = request.form.get("descricao")
    marca = request.form.get("marca")
    modelo = request.form.get("modelo")
    tipo = request.form.get("tipo")
    cor = request.form.get("cor")
    lancamento = request.form.get("lancamento")
    codigo = request.form.get("codigo")
    status = request.form.get("status")

    print(f"descricao: {descricao}")
    print(f"marca: {marca}")
    print(f"modelo: {modelo}")
    print(f"tipo: {tipo}")
    print(f"cor: {cor}")
    print(f"lancamento: {lancamento}")
    print(f"codigo: {codigo}")
    print(f"status: {status}")
    
    novo_equipamento = Equipamento(
        descricao=descricao,
        marca=marca,
        modelo=modelo,
        tipo=tipo,
        cor=cor,
        lancamento=lancamento,
        codigo=codigo,
        status=status,
    )
    
    db.session.add(novo_equipamento)
    db.session.commit()
    
    return redirect(url_for("auth.total_equipamentos"))

@auth_bp.route("/total_equipamentos")
def total_equipamentos():
    equipamentos = Equipamento.query.all()
    return render_template("total_de_equipamentos.html", equipamentos=equipamentos)

@auth_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@auth_bp.route("/lista")
def lista():
    equipamentos = Equipamento.query.filter(
    Equipamento.status != "Desativado"
).all()
    return render_template("lista_de_equipamentos.html", equipamentos=equipamentos)

@auth_bp.route("/editar/<int:id>")
def editar_equipamento(id):
    equipamento = Equipamento.query.get(id)
    return render_template("cadastro.html", equipamento=equipamento)

@auth_bp.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):

    equipamento = Equipamento.query.get(id)

    equipamento.descricao = request.form["descricao"]
    equipamento.marca = request.form["marca"]
    equipamento.modelo = request.form["modelo"]
    equipamento.tipo = request.form["tipo"]
    equipamento.cor = request.form["cor"]
    equipamento.lancamento = request.form["lancamento"]
    equipamento.codigo = request.form["codigo"]
    equipamento.status = request.form["status"]

    db.session.commit()

    return redirect(url_for("auth.lista"))

@auth_bp.route("/equipamento/<tipo>")
def equipamentos_por_tipo(tipo):
    equipamentos = Equipamento.query.filter_by(tipo=tipo).all()
    return render_template("equipamento.html", equipamentos=equipamentos, tipo=tipo)

@auth_bp.route("/marca/<marca>")
def marca(marca):
    equipamentos = Equipamento.query.filter_by(marca=marca).all()
    return render_template("marca.html", equipamentos=equipamentos, marca=marca)

@auth_bp.route("/desativados")
def desativados():

    equipamentos = Equipamento.query.filter_by(
        status="Desativado"
    ).all()

    return render_template(
        "desativados.html",
        equipamentos=equipamentos
    )

@auth_bp.route("/desativar/<int:id>")
def desativar(id):

    equipamento = Equipamento.query.get(id)

    if equipamento:
        equipamento.status = "Desativado"
        db.session.commit()

    return redirect(url_for("auth.lista"))

@auth_bp.route('/reativar/<int:id>')
def reativar(id):

    equipamento = Equipamento.query.get_or_404(id)

    equipamento.status = 'Ativo'

    db.session.commit()

    return redirect(url_for('auth.desativados'))
