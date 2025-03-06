from app import db
from app.models.objects.usuario import Usuario

class Paciente(Usuario):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)