from app.models.dao.usuario_dao import UsuarioDAO, Usuario
from app.models.dao.enfermera_dao import EnfermeraDAO, Enfermera
from app.models.dao.medico_dao import MedicoDAO, Medico
from app.models.dao.paciente_dao import PacienteDAO, Paciente
from app.models.dao.administrador_dao import AdministradorDAO, Administrador
from werkzeug.security import check_password_hash

usuario_dao = UsuarioDAO()
enfermera_dao = EnfermeraDAO()
medico_dao = MedicoDAO()
paciente_dao = PacienteDAO()
administrador_dao = AdministradorDAO()

# USUARIOS

def crear_usuario(nombre, password, rol):
    entity = Usuario(nombre=nombre, rol=rol)
    return usuario_dao.insert(entity, password)

def obtener_usuarios():
    return usuario_dao.get_all()

def obtener_usuario_por_id(usuario_id):
    return usuario_dao.get_by_id(usuario_id)

def obtener_usuario_por_login(nombre, password):
    return usuario_dao.verify_user(nombre, password)

def actualizar_usuario(usuario_id, nombre):
    usuario = usuario_dao.get_by_id(usuario_id)
    if usuario:
        usuario.nombre = nombre
        usuario_dao.update()
        return usuario
    return None

def eliminar_usuario(usuario_id):
    usuario = usuario_dao.get_by_id(usuario_id)
    if usuario:
        usuario_dao.delete(usuario)
        return True
    return False

# ENFERMERA

def crear_enfermera(nombre, password):
    entity = Enfermera(nombre=nombre, rol="enfermera")
    return enfermera_dao.insert(entity, password)
    
def obtener_enfermeras():
    return enfermera_dao.get_all()

def obtener_enfermera_por_id(entity_id):
    return enfermera_dao.get_by_id(entity_id)

def actualizar_enfermera(entity_id, nombre):
    return enfermera_dao.update_by_id(entity_id, nombre)

def eliminar_enfermera(entity_id):
    return enfermera_dao.delete_by_id(entity_id)

# MEDICO

def crear_medico(nombre, password, especialidad):
    entity = Medico(nombre=nombre, rol='medico', especialidad=especialidad)
    return medico_dao.insert(entity, password)

def obtener_medicos():
    return medico_dao.get_all()

def obtener_medico_por_id(entity_id):
    return medico_dao.get_by_id(entity_id)

def actualizar_medico(entity_id, nombre, especialidad):
    return medico_dao.update_by_id(entity_id, nombre, especialidad)

def eliminar_medico(entity_id):
    return medico_dao.delete_by_id(entity_id)

# ADMINISTRADOR

def crear_administrador(nombre, password):
    entity = Administrador(nombre=nombre, rol="administrador")
    return administrador_dao.insert(entity, password)
    
def obtener_administradores():
    return administrador_dao.get_all()

def obtener_administrador_por_id(entity_id):
    return administrador_dao.get_by_id(entity_id)

def actualizar_administrador(entity_id, nombre):
    return administrador_dao.update_by_id(entity_id, nombre)

def eliminar_administrador(entity_id):
    return administrador_dao.delete_by_id(entity_id)
   
# PACIENTE

def crear_paciente(nombre, password):
    entity = Paciente(nombre=nombre, rol="paciente")
    return paciente_dao.insert(entity, password)
    
def obtener_pacientes():
    return paciente_dao.get_all()

def obtener_paciente_por_id(entity_id):
    return paciente_dao.get_by_id(entity_id)

def actualizar_paciente(entity_id, nombre):
    return paciente_dao.update_by_id(entity_id, nombre)

def eliminar_paciente(entity_id):
    return paciente_dao.delete_by_id(entity_id)