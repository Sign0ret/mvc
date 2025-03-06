from flask import Blueprint, render_template, request, redirect, url_for, abort, jsonify, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.objects.usuario import Usuario, db
from app.models.objects.paciente import Paciente
from app.controllers.cita_controller import crear_cita, obtener_todas_las_citas
from app.controllers.usuario_controller import (
    crear_usuario , obtener_usuarios, obtener_usuario_por_login, actualizar_usuario, eliminar_usuario,
    crear_administrador , obtener_administradores, actualizar_administrador, eliminar_administrador,
    crear_enfermera , obtener_enfermeras, actualizar_enfermera, eliminar_enfermera,
    crear_medico , obtener_medicos, actualizar_medico, eliminar_medico,
    crear_paciente , obtener_pacientes, actualizar_paciente, eliminar_paciente,
)
from app.decorators import role_required

bp = Blueprint('routes', __name__)

# Rutas Auth
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        user = obtener_usuario_por_login(nombre=nombre, password=password)
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('routes.index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        crear_paciente(nombre=nombre, password=password)
        flash('Registration successful. Please log in.')
        return redirect(url_for('routes.login'))
    return render_template('register.html')

# Ruta Default

@bp.route('/')
@login_required
def index():
    return redirect(url_for('routes.ver_citas'))

# Rutas Citas

@bp.route('/citas', methods=['GET', 'POST'])
@login_required
@role_required(['administrador', 'enfermera', 'medico', 'paciente'])
def ver_citas():
    """ Vista para ver y agendar citas, filtrando según el rol del usuario """
    # Obtener citas según el rol del usuario
    if current_user.rol in ['administrador', 'enfermera']:
        citas = obtener_todas_las_citas()
        medicos = obtener_medicos()
        pacientes = obtener_pacientes()
    elif current_user.rol == 'medico':
        citas = [cita for cita in obtener_todas_las_citas() if cita.medico_id == current_user.id]
        medicos = None
        pacientes = obtener_pacientes()
    elif current_user.rol == 'paciente':
        citas = [cita for cita in obtener_todas_las_citas() if cita.paciente_id == current_user.id]
        medicos = obtener_medicos()
        pacientes = None
    else:
        abort(403)  # Forbidden

    # Si se envía el formulario, intentar crear una cita
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora = request.form['hora']
        motivo = request.form['motivo']

        if current_user.rol in ['administrador', 'enfermera']:
            medico_id = request.form['medico_id']
            paciente_id = request.form['paciente_id']
        elif current_user.rol == 'medico':
            medico_id = current_user.id
            paciente_id = request.form['paciente_id']
        elif current_user.rol == 'paciente':
            medico_id = request.form['medico_id']
            paciente_id = current_user.id
        else:
            abort(403)  # Forbidden
        crear_cita(fecha, hora, motivo, paciente_id, medico_id)
        return redirect(url_for('routes.ver_citas'))
    
    return render_template('citas.html', citas=citas, medicos=medicos, pacientes=pacientes, current_user=current_user)


@bp.route('/aceptar_cita/<int:cita_id>', methods=['POST'])
@login_required
@role_required(['medico'])
def aceptar_cita(cita_id):
    """ Permite a un médico aceptar una cita """
    cita = obtener_cita_por_id(cita_id)

    if not cita:
        flash('La cita no existe', 'danger')
        return redirect(url_for('routes.ver_citas'))

    if cita.medico_id != current_user.id:
        abort(403)  # Forbidden, el médico solo puede aceptar sus propias citas

    actualizar_estado_cita(cita_id, "Aceptada")
    flash('Cita aceptada exitosamente', 'success')
    
    return redirect(url_for('routes.ver_citas'))


# Rutas Usuarios

@bp.route('/<tipo>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
@role_required(['administrador'])
def gestionar_usuarios(tipo):
    if tipo not in ['administradores', 'enfermeras', 'pacientes', 'medicos']:
        abort(404)  # Invalid user type

    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        if tipo == 'administradores':
            crear_administrador(nombre=nombre, password=password)
        elif tipo == 'enfermeras':
            crear_enfermera(nombre=nombre, password=password)
        elif tipo == 'pacientes':
            crear_paciente(nombre=nombre, password=password)
        elif tipo == 'medicos':
            especialidad = request.form['especialidad']
            crear_medico(nombre=nombre, password=password, especialidad=especialidad)
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