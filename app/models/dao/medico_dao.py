from .abstract_dao import AbstractDAO
from app.models.objects.medico import Medico
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class MedicoDAO(AbstractDAO):
    def __init__(self):
        super().__init__(Medico)

    def insert(self, entity, password):
        entity.password_hash = generate_password_hash(password)
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self):
        db.session.commit()

    def update_by_id(self, entity_id, nombre, especialidad):
        entity = self.model.query.get(entity_id)
        if entity:
            entity.nombre = nombre
            entity.especialidad = especialidad
            db.session.commit()
            return entity
        return None
    
    def delete(self, entity):
        db.session.delete(entity)
        db.session.commit()
    
    def delete_by_id(self, entity_id):
        entity = self.model.query.get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False

    def get_by_id(self, entity_id):
        return self.model.query.get(entity_id)

    def get_all(self):
        return self.model.query.all()