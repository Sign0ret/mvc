from flask import Blueprint, render_template, request, redirect, url_for
from .controllers import crear_usuario, crear_cita, obtener_usuarios, obtener_citas

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return redirect(url_for('routes.ver_usuarios'))

@bp.route('/usuarios')
def ver_usuarios():
    usuarios = obtener_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)

@bp.route('/citas')
def ver_citas():
    citas = obtener_citas()
    return render_template('citas.html', citas=citas)

@bp.route('/usuarios', methods=['POST'])
def agregar_usuario():
    nombre = request.form['nombre']
    rol = request.form['rol']
    crear_usuario(nombre=nombre, rol=rol)
    return redirect(url_for('routes.ver_usuarios'))

@bp.route('/citas', methods=['POST'])
def agregar_cita():
    fecha = request.form['fecha']
    hora = request.form['hora']
    motivo = request.form['motivo']
    medico_id = request.form['medico_id']
    paciente_id = request.form['paciente_id']
    crear_cita(fecha=fecha, hora=hora, motivo=motivo, paciente_id=paciente_id, medico_id=medico_id)
    return redirect(url_for('routes.ver_citas'))