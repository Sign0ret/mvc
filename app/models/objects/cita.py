from app import db

class Cita(db.Model):
    __tablename__ = 'cita'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(5), nullable=False)
    motivo = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(50), default="Pendiente")

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