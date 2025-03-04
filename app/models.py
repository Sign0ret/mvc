from . import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def autenticar(self):
        return f"Usuario {self.nombre} autenticado."

    def cerrar_sesion(self):
        return f"Usuario {self.nombre} cerró sesión."

class Administrador(Usuario):
    __tablename__ = 'administrador'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    def gestionar_cita(self, cita):
        return f"Gestionando cita: {cita.motivo}"

    def gestionar_horario_medico(self, medico):
        return f"Gestionando horario del médico: {medico.nombre}"

    def gestionar_paciente(self, paciente):
        return f"Gestionando paciente: {paciente.nombre}"

class Medico(Usuario):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    especialidad = db.Column(db.String(100), nullable=False)

    def revisar_cita(self, cita):
        return f"Revisando cita: {cita.motivo}"

    def aceptar_cita(self, cita):
        cita.estado = "Aceptada"
        return f"Cita aceptada: {cita.motivo}"

    def actualizar_estado_consulta(self, cita, nuevo_estado):
        cita.estado = nuevo_estado
        return f"Estado actualizado a: {nuevo_estado}"

class Enfermera(Usuario):
    __tablename__ = 'enfermera'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    def actualizar_estado_cita(self, cita, nuevo_estado):
        cita.estado = nuevo_estado
        return f"Estado actualizado por la enfermera a: {nuevo_estado}"

    def registrar_signos_vitales(self, paciente, signos_vitales):
        return f"Signos vitales registrados para el paciente {paciente.nombre}: {signos_vitales}"

class Paciente(Usuario):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)

    def agendar_cita(self, fecha, hora, motivo):
        return f"Cita agendada para el paciente {self.nombre} en la fecha {fecha} a las {hora} con motivo: {motivo}"

    def ver_estado_citas(self, citas):
        return [f"Cita: {cita.motivo}, Estado: {cita.estado}" for cita in citas]

class Cita(db.Model):
    __tablename__ = 'cita'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(5), nullable=False)
    motivo = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(50), default="Pendiente")
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
