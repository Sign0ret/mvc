from flask import Blueprint, render_template, request, redirect, url_for, abort, jsonify
from app.controllers.cita import crear_cita, actualizar_estado_cita, obtener_citas
from app.controllers.usuario import (
    crear_usuario , obtener_usuarios, actualizar_usuario, eliminar_usuario,
    crear_administrador , obtener_administradores, actualizar_administrador, eliminar_administrador,
    crear_enfermera , obtener_enfermeras, actualizar_enfermera, eliminar_enfermera,
    crear_medico , obtener_medicos, actualizar_medico, eliminar_medico,
    crear_paciente , obtener_pacientes, actualizar_paciente, eliminar_paciente,
)

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return redirect(url_for('routes.ver_citas'))

# Rutas Citas

@bp.route('/citas', methods=['GET', 'POST'])
def ver_citas():
    # Obtener citas, médicos y pacientes
    citas = obtener_citas()
    medicos = obtener_medicos()
    pacientes = obtener_pacientes()

    if request.method == 'POST':
        fecha = request.form['fecha']
        hora = request.form['hora']
        motivo = request.form['motivo']
        medico_id = request.form['medico_id']
        paciente_id = request.form['paciente_id']
        crear_cita(fecha=fecha, hora=hora, motivo=motivo, paciente_id=paciente_id, medico_id=medico_id)
        return redirect(url_for('routes.ver_citas'))
    
    return render_template('citas.html', citas=citas, medicos=medicos, pacientes=pacientes)

# Rutas Usuarios

@bp.route('/<tipo>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gestionar_usuarios(tipo):
    if tipo not in ['administradores', 'medicos', 'enfermeras', 'pacientes']:
        abort(404)  # Invalid user type

    if request.method == 'POST':
        nombre = request.form['nombre']
        if tipo == 'administradores':
            crear_administrador(nombre=nombre)
        elif tipo == 'enfermeras':
            crear_enfermera(nombre=nombre)
        elif tipo == 'pacientes':
            crear_paciente(nombre=nombre)
        elif tipo == 'medicos':
            especialidad = request.form['especialidad']
            crear_medico(nombre=nombre, especialidad=especialidad)
        return redirect(url_for('routes.gestionar_usuarios', tipo=tipo))

    if request.method == 'PUT':
        # Get the JSON data from the request
        data = request.get_json()
        user_id = data['id']
        nombre = data.get('nombre')
        especialidad = data.get('especialidad', None)

        # Handle different types of users
        if tipo == 'administradores':
            actualizar_administrador(user_id, nombre)
        elif tipo == 'enfermeras':
            actualizar_enfermera(user_id, nombre)
        elif tipo == 'pacientes':
            actualizar_paciente(user_id, nombre)
        elif tipo == 'medicos':
            actualizar_medico(user_id, nombre, especialidad)

        return jsonify({"success": True}), 200

    if request.method == 'DELETE':
        data = request.get_json()  # Get JSON data from request
        user_id = data.get('id')  # Extract ID
        if not user_id:
            abort(400, description="Missing user ID")

        if tipo == 'administradores':
            eliminar_administrador(user_id)
        elif tipo == 'enfermeras':
            eliminar_enfermera(user_id)
        elif tipo == 'pacientes':
            eliminar_paciente(user_id)
        elif tipo == 'medicos':
            eliminar_medico(user_id)
        else:
            abort(400)  # Invalid type
        
        return jsonify({"success": True}), 204  # Return a success response

    if tipo == 'administradores':
        usuarios = obtener_administradores()
    elif tipo == 'enfermeras':
        usuarios = obtener_enfermeras()
    elif tipo == 'pacientes':
        usuarios = obtener_pacientes()
    elif tipo == 'medicos':
        usuarios = obtener_medicos()

    return render_template('usuarios.html', tipo=tipo, usuarios=usuarios)