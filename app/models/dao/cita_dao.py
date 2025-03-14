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

    def update_by_id(self, entity_id, estado):
        entity = self.model.query.get(entity_id)
        if entity:
            entity.estado = estado
            db.session.commit()
            return entity
        return None

    def edit_by_id(self, entity_id, fecha, hora, motivo):
        print("lo intento")
        entity = self.model.query.get(entity_id)
        if entity:
            entity.fecha = fecha
            entity.hora = hora
            entity.motivo = motivo
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
