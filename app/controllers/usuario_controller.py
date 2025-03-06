from app.models.dao.usuario_dao import UsuarioDAO, Usuario
from app.models.dao.enfermera_dao import EnfermeraDAO, Enfermera
from app.models.dao.medico_dao import MedicoDAO, Medico
from app.models.dao.paciente_dao import PacienteDAO, Paciente
from app.models.dao.administrador_dao import AdministradorDAO, Administrador

from app import db

from werkzeug.security import check_password_hash

# USUARIOS

def crear_usuario(nombre, password, rol):
    return usuario_dao.insert_usuario(nombre, password, rol)

def obtener_usuarios():
    return usuario_dao.get_all()

def obtener_usuario_por_login(nombre, password):
    return usuario_dao.verify_user(nombre, password)

def obtener_usuario_por_id(usuario_id):
    return usuario_dao.get_by_id(usuario_id)

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
    nueva_enfermera = Enfermera(nombre=nombre, rol='enfermera')
    nueva_enfermera.set_password(password)
    db.session.add(nueva_enfermera)
    db.session.commit()
    return nueva_enfermera
    
def obtener_enfermeras():
    return Enfermera.query.all()

def obtener_enfermera_por_id(enfermera_id):
    return Enfermera.query.get(enfermera_id)

def actualizar_enfermera(enfermera_id, nombre):
    enfermera = Enfermera.query.get(enfermera_id)
    if enfermera:
        enfermera.nombre = nombre
        db.session.commit()
        return enfermera
    return None

def eliminar_enfermera(enfermera_id):
    db.session.delete(Enfermera.query.get(enfermera_id))
    db.session.commit()
    return True

# MEDICO

def crear_medico(nombre, password, especialidad):
    nuevo_medico = Medico(nombre=nombre, rol='medico', especialidad=especialidad)
    nuevo_medico.set_password(password)
    db.session.add(nuevo_medico)
    db.session.commit()
    return nuevo_medico

def obtener_medicos():
    return Medico.query.all()

def obtener_medico_por_id(medico_id):
    return Medico.query.get(medico_id)

def actualizar_medico(medico_id, nombre, especialidad):
    medico = Medico.query.get(medico_id)
    if medico:
        medico.nombre = nombre
        medico.especialidad = especialidad
        db.session.commit()
        return medico
    return None

def eliminar_medico(medico_id):
    db.session.delete(Medico.query.get(medico_id))
    db.session.commit()
    return True

# ADMINISTRADOR

def crear_administrador(nombre, password):
    nuevo_admin = Administrador(nombre=nombre, rol='administrador')
    nuevo_admin.set_password(password)
    db.session.add(nuevo_admin)
    db.session.commit()
    return nuevo_admin

def obtener_administradores():
    return Administrador.query.all()

def obtener_administrador_por_id(admin_id):
    return Administrador.query.get(admin_id)

def actualizar_administrador(admin_id, nombre):
    admin = Administrador.query.get(admin_id)
    if admin:
        admin.nombre = nombre
        db.session.commit()
        return admin
    return None

def eliminar_administrador(admin_id):
    db.session.delete(Administrador.query.get(admin_id))
    db.session.commit()
    return True
   
# PACIENTE

def crear_paciente(nombre, password):
    nuevo_paciente = Paciente(nombre=nombre, rol='paciente')
    nuevo_paciente.set_password(password)
    db.session.add(nuevo_paciente)
    db.session.commit()
    return nuevo_paciente

def obtener_pacientes():
    return Paciente.query.all()

def obtener_paciente_por_id(paciente_id):
    return Paciente.query.get(paciente_id)

def actualizar_paciente(paciente_id, nombre):
    paciente = Paciente.query.get(paciente_id)
    if paciente:
        paciente.nombre = nombre
        db.session.commit()
        return paciente
    return None

def eliminar_paciente(paciente_id):
    db.session.delete(Paciente.query.get(paciente_id))
    db.session.commit()
    return True