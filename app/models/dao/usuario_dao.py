from .abstract_dao import AbstractDAO
from app.models.objects.usuario import Usuario
from app import db

class UsuarioDAO(AbstractDAO):
    def __init__(self):
        super().__init__(Usuario)

    def insert(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self):
        db.session.commit()

    def delete(self, entity):
        db.session.delete(entity)
        db.session.commit()

    def get_by_id(self, entity_id):
        return Usuario.query.get(entity_id)

    def get_all(self):
        return Usuario.query.all()

    # Nuevas
    
    def insert_usuario(self, nombre, password, rol):
        """Create and store a user with an encrypted password"""
        nuevo_usuario = Usuario(nombre=nombre, rol=rol)
        nuevo_usuario.password_hash = generate_password_hash(password)  # Encrypt the password
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario

    def get_by_name(self, nombre):
        """Retrieve a user by their name"""
        return Usuario.query.filter_by(nombre=nombre).first()

    def verify_user(self, nombre, password):
        """Verify user credentials"""
        usuario = self.get_by_name(nombre)
        if usuario and check_password_hash(usuario.password_hash, password):
            return usuario
        return None
