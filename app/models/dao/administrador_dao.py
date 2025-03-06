from .abstract_dao import AbstractDAO
from app.models.objects.administrador import Administrador
from app import db

class AdministradorDAO(AbstractDAO):
    def __init__(self):
        super().__init__(Administrador)

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
        return Administrador.query.get(entity_id)

    def get_all(self):
        return Administrador.query.all()