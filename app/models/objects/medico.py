from app import db
from app.models.objects.usuario import Usuario

class Medico(Usuario):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    especialidad = db.Column(db.String(100), nullable=False)
    