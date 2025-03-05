from app.models import Cita, db

def crear_cita(fecha, hora, motivo, paciente_id, medico_id):
    nueva_cita = Cita(fecha=fecha, hora=hora, motivo=motivo, paciente_id=paciente_id, medico_id=medico_id)
    db.session.add(nueva_cita)
    db.session.commit()
    return nueva_cita

def actualizar_estado_cita(cita_id, nuevo_estado):
    cita = Cita.query.get(cita_id)
    if not cita:
        return None
    cita.estado = nuevo_estado
    db.session.commit()
    return cita

def obtener_citas():
    return Cita.query.all()