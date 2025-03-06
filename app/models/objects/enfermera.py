from app import db
from app.models.objects.usuario import Usuario

class Enfermera(Usuario):
    __tablename__ = 'enfermera'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)