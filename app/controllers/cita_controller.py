from app.models.dao.cita_dao import CitaDAO
from app.models.objects.cita import Cita

cita_dao = CitaDAO()

def crear_cita(fecha, hora, motivo, paciente_id, medico_id):
    nueva_cita = Cita(fecha=fecha, hora=hora, motivo=motivo, paciente_id=paciente_id, medico_id=medico_id)
    return cita_dao.insert(nueva_cita)

def obtener_cita_por_id(cita_id):
    return cita_dao.get_by_id(cita_id)

def obtener_todas_las_citas():
    return cita_dao.get_all()

def actualizar_estado_cita(cita_id, nuevo_estado):
    cita = cita_dao.get_by_id(cita_id)
    if cita:
        cita.estado = nuevo_estado
        cita_dao.update()
        return cita
    return None

def eliminar_cita(cita_id):
    cita = cita_dao.get_by_id(cita_id)
    if cita:
        cita_dao.delete(cita)
        return True
    return False