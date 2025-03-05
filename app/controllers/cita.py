from app.models import Cita, db

def crear_cita(fecha, hora, motivo, paciente_id, medico_id):
    nueva_cita = Cita(fecha=fecha, hora=hora, motivo=motivo, paciente_id=paciente_id, medico_id=medico_id)
    db.session.add(nueva_cita)
    db.session.commit()
    return nueva_cita

def obtener_citas():
    return Cita.query.all()

def obtener_citas_por_medico(id):
    return Cita.query.filter(Cita.medico_id == id).all()

def obtener_citas_por_paciente(id):
    return Cita.query.filter(Cita.paciente_id == id).all()

def validar_cita(cita_id):
    cita = Cita.query.get(cita_id)
    if not cita:
        return None
    cita.estado = 'Aceptada'
    db.session.commit()
    return cita