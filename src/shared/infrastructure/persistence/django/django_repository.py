# -*- coding: utf8 -*-


from src.shared.domain.repository import AbstractRepository

from django.db.models import Model


class DjangoRepository(AbstractRepository):
    def __init__(self):
        self.model = Model

    def add(self, entity):
        pass

    def edit(self, entity):
        pass

    def delete(self, entity):
        pass
