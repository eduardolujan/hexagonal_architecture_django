# -*- coding: utf8 -*-


from django.db.models import Model

from src.shared.domain.repository import AbstractRepository
from .django_orm_manager import DjangoOrmManager
from src.shared.domain.entities import Entity


class DjangoRepository(DjangoOrmManager, AbstractRepository):
    model = Model

    def get(self, entity):
        """
        Get instance by fields
        """
        if not entity:
            raise ValueError('Entity is null')
        self.django_read(entity.as_dict())

    def create(self, **fields):
        try:
            model_instance = self.model()
            for field, value in fields.items():
                setattr(model_instance, field, value)
            model_instance.save()
        except Exception as err:
            message = str(err)

    def update(self, **fields):
        pass

    def delete(self, **fields):
        pass

    def search(self, **fields):
        pass

    def all(self):
        pass
