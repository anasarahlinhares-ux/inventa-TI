from . import db

class Equipamento(db.Model):
    __tablename__ = 'equipamentos'
    
    id = db.Column(db.Integer, primary_key=True)  # ADICIONA NOME!
    descricao = db.Column(db.String(200), nullable=False)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    tipo = db.Column(db.String(50))
    cor = db.Column(db.String(30))
    lancamento = db.Column(db.String(20))  # SEM ACENTO!
    codigo = db.Column(db.String(30))
    status = db.Column(db.String(20))  # ADICIONA EMPRESA!
    
    def __repr__(self):
        return f'<Equipamento {self.nome}>'