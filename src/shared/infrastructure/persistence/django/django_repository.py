# -*- coding: utf8 -*-


from django.db.models import Model

from src.shared.domain.repository import AbstractRepository
from src.shared.domain.entities import Entity
from .django_orm_manager import DjangoOrmManager


class DjangoRepository(DjangoOrmManager, AbstractRepository):
    def __init__(self):
        super(DjangoRepository, self).__init__(self.entity, self.model)

    def get(self, entity):
        if not entity:
            raise ValueError('Entity is null')
        return self.get_orm(**entity.as_dict())

    def create(self, entity):
        model_instance = self.orm_create(**entity.as_dict())
        self.seen.add(model_instance)
        return True

    def update(self, entity: Entity):
        model_instance = self.orm_update(**entity.as_dict())
        self.seen.add(model_instance)
        return True

    def delete(self, entity: Entity):
        model_instance = self.orm_update(**entity.as_dict())
        self.seen.add(model_instance)
        return True

    def search(self, entity: Entity):
        return self.search(**entity.as_dict())

    def all(self):
        """
        Get all instances
        """
        return self.orm_all()
