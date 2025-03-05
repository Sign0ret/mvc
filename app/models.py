from . import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    # TODO
    def autenticar(self):
        return f"Usuario {self.nombre} autenticado."
    # TODO
    def cerrar_sesion(self):
        return f"Usuario {self.nombre} cerró sesión."

class Administrador(Usuario):
    __tablename__ = 'administrador'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    # TODO
    def gestionar_cita(self, cita):
        return f"Gestionando cita: {cita.motivo}"
    # TODO
    def gestionar_horario_medico(self, medico):
        return f"Gestionando horario del médico: {medico.nombre}"
    # TODO
    def gestionar_paciente(self, paciente):
        return f"Gestionando paciente: {paciente.nombre}"

class Medico(Usuario):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    especialidad = db.Column(db.String(100), nullable=False)
    # TODO
    def revisar_cita(self, cita):
        return f"Revisando cita: {cita.motivo}"
    # TODO
    def aceptar_cita(self, cita):
        cita.estado = "Aceptada"
        return f"Cita aceptada: {cita.motivo}"
    # TODO
    def actualizar_estado_consulta(self, cita, nuevo_estado):
        cita.estado = nuevo_estado
        return f"Estado actualizado a: {nuevo_estado}"

class Enfermera(Usuario):
    __tablename__ = 'enfermera'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    # TODO
    def actualizar_estado_cita(self, cita, nuevo_estado):
        cita.estado = nuevo_estado
        return f"Estado actualizado por la enfermera a: {nuevo_estado}"

class Paciente(Usuario):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    # TODO
    def agendar_cita(self, fecha, hora, motivo):
        return f"Cita agendada para el paciente {self.nombre} en la fecha {fecha} a las {hora} con motivo: {motivo}"
    # TODO
    def ver_estado_citas(self, citas):
        return [f"Cita: {cita.motivo}, Estado: {cita.estado}" for cita in citas]

class Cita(db.Model):
    __tablename__ = 'cita'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(5), nullable=False)
    motivo = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(50), default="Pendiente")
    
    # Claves foráneas con nombres explícitos
    paciente_id = db.Column(
        db.Integer, 
        db.ForeignKey('paciente.id', name='fk_cita_paciente_id'), 
        nullable=False
    )
    
    medico_id = db.Column(
        db.Integer, 
        db.ForeignKey('medico.id', name='fk_cita_medico_id'), 
        nullable=False
    )
    # TODO
    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado