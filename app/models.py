from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Administrador(Usuario):
    __tablename__ = 'administrador'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

class Medico(Usuario):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    especialidad = db.Column(db.String(100), nullable=False)

class Enfermera(Usuario):
    __tablename__ = 'enfermera'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

class Paciente(Usuario):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

class Cita(db.Model):
    __tablename__ = 'cita'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(5), nullable=False)
    motivo = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(50), default="Pendiente")
    
    # Claves foráneas con nombres explícitos
    paciente_id = db.Column(
        db.Integer, 
        db.ForeignKey('paciente.id', name='fk_cita_paciente_id'), 
        nullable=False
    )
    
    medico_id = db.Column(
        db.Integer, 
        db.ForeignKey('medico.id', name='fk_cita_medico_id'), 
        nullable=False
    )