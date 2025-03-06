from app import db
from app.models.objects.usuario import Usuario

class Administrador(Usuario):
    __tablename__ = 'administrador'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)