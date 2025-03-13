from app.models.dao.cita_dao import CitaDAO
from app.models.objects.cita import Cita

cita_dao = CitaDAO()

def crear_cita(fecha, hora, motivo, paciente_id, medico_id):
    entity = Cita(fecha=fecha, hora=hora, motivo=motivo, paciente_id=paciente_id, medico_id=medico_id)
    return cita_dao.insert(entity)

def obtener_citas():
    return cita_dao.get_all()

def obtener_cita_por_id(entity_id):
    return cita_dao.get_by_id(entity_id)

def actualizar_cita(entity_id, estado):
    return cita_dao.update_by_id(entity_id, estado)

def editar_cita(entity_id, fecha, hora, motivo):
    return cita_dao.edit_by_id(entity_id, fecha, hora, motivo)

def eliminar_cita(entity_id):
    return cita_dao.delete_by_id(entity_id)