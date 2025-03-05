from app.models import Usuario, Enfermera, Medico, Administrador, Paciente, db

def crear_usuario(nombre, rol):
    nuevo_usuario = Usuario(nombre=nombre, rol=rol)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return nuevo_usuario

def crear_enfermera(nombre):
    nueva_enfermera = Enfermera(nombre=nombre, rol='enfermera')
    db.session.add(nueva_enfermera)
    db.session.commit()
    return nueva_enfermera

def crear_medico(nombre, especialidad):
    nuevo_medico = Medico(nombre=nombre, rol='medico', especialidad=especialidad)
    db.session.add(nuevo_medico)
    db.session.commit()
    return nuevo_medico

def crear_administrador(nombre):
    nuevo_admin = Administrador(nombre=nombre, rol='administrador')
    db.session.add(nuevo_admin)
    db.session.commit()
    return nuevo_admin

def crear_paciente(nombre):
    nuevo_paciente = Paciente(nombre=nombre, rol='paciente')
    db.session.add(nuevo_paciente)
    db.session.commit()
    return nuevo_paciente

# Funciones para obtener usuarios
def obtener_usuarios():
    return Usuario.query.all()

def obtener_enfermeras():
    return Enfermera.query.all()

def obtener_medicos():
    return Medico.query.all()

def obtener_administradores():
    return Administrador.query.all()

def obtener_pacientes():
    return Paciente.query.all()

# Funciones adicionales para obtener un usuario específico por ID
def obtener_usuario_por_id(usuario_id):
    return Usuario.query.get(usuario_id)

def obtener_enfermera_por_id(enfermera_id):
    return Enfermera.query.get(enfermera_id)

def obtener_medico_por_id(medico_id):
    return Medico.query.get(medico_id)

def obtener_administrador_por_id(admin_id):
    return Administrador.query.get(admin_id)

def obtener_paciente_por_id(paciente_id):
    return Paciente.query.get(paciente_id)

# Funciones para actualizar usuarios
def actualizar_usuario(usuario_id, nombre):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        usuario.nombre = nombre
        db.session.commit()
        return usuario
    return None

def actualizar_enfermera(enfermera_id, nombre):
    enfermera = Enfermera.query.get(enfermera_id)
    if enfermera:
        enfermera.nombre = nombre
        db.session.commit()
        return enfermera
    return None

def actualizar_medico(medico_id, nombre, especialidad):
    medico = Medico.query.get(medico_id)
    if medico:
        medico.nombre = nombre
        medico.especialidad = especialidad
        db.session.commit()
        return medico
    return None

def actualizar_administrador(admin_id, nombre):
    admin = Administrador.query.get(admin_id)
    if admin:
        admin.nombre = nombre
        db.session.commit()
        return admin
    return None

def actualizar_paciente(paciente_id, nombre):
    paciente = Paciente.query.get(paciente_id)
    if paciente:
        paciente.nombre = nombre
        db.session.commit()
        return paciente
    return None

# Funciones para eliminar usuarios
def eliminar_usuario(usuario_id):
    db.session.delete(Usuario.query.get(usuario_id))
    db.session.commit()
    return True

def eliminar_enfermera(enfermera_id):
    db.session.delete(Enfermera.query.get(enfermera_id))
    db.session.commit()
    return True

def eliminar_medico(medico_id):
    db.session.delete(Medico.query.get(medico_id))
    db.session.commit()
    return True

def eliminar_administrador(admin_id):
    db.session.delete(Administrador.query.get(admin_id))
    db.session.commit()
    return True

def eliminar_paciente(paciente_id):
    db.session.delete(Paciente.query.get(paciente_id))
    db.session.commit()
    return True
