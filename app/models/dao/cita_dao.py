from .abstract_dao import AbstractDAO
from app.models.objects.cita import Cita
from app import db

class CitaDAO(AbstractDAO):
    def __init__(self):
        super().__init__(Cita)

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
        return Cita.query.get(entity_id)

    def get_all(self):
        return Cita.query.all()
