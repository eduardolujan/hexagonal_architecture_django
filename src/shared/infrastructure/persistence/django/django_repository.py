# -*- coding: utf8 -*-


from django.db.models import Model

from src.shared.domain.repository import AbstractRepository
from .django_orm_manager import DjangoOrmManager


class DjangoRepository(DjangoOrmManager, AbstractRepository):
    def __init__(self):
        super(DjangoRepository, self).__init__(self.entity, self.model)

    def get(self, entity):
        """
        Get instance by fields dict
        """
        if not entity:
            raise ValueError('Entity is null')
        return self.get_orm(**entity.as_dict())

    def create(self, entity):
        pass

    def update(self, entity):
        pass

    def delete(self, entity):
        pass

    def search(self, entity):
        pass

    def all(self):
        """
        Get all instances
        """
        return self.orm_all()
