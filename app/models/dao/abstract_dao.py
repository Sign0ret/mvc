from abc import ABC, abstractmethod
from app import db

class AbstractDAO(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def insert(self, entity):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def update_by_id(self, entity_id):
        pass

    @abstractmethod
    def delete(self, entity):
        pass

    @abstractmethod
    def delete_by_id(self, entity_id):
        pass

    @abstractmethod
    def get_by_id(self, entity_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

# def create_dao_class(model):
#     class GenericDAO(AbstractDAO):
#         def __init__(self):
#             super().__init__(model)

#         def insert(self, entity):
#             db.session.add(entity)
#             db.session.commit()
#             return entity

#         def update(self):
#             db.session.commit()

#         def delete(self, entity):
#             db.session.delete(entity)
#             db.session.commit()

#         def get_by_id(self, entity_id):
#             return model.query.get(entity_id)

#         def get_all(self):
#             return model.query.all()

#     return GenericDAO