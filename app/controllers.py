from .models import Usuario, Cita, Paciente, Medico, Administrador, Enfermera, db

def crear_usuario(nombre, rol):
    nuevo_usuario = Usuario(nombre=nombre, rol=rol)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return nuevo_usuario

def crear_cita(fecha, hora, motivo, paciente_id):
    nueva_cita = Cita(fecha=fecha, hora=hora, motivo=motivo, paciente_id=paciente_id)
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

def obtener_usuarios():
    return Usuario.query.all()

def obtener_citas():
    return Cita.query.all()

