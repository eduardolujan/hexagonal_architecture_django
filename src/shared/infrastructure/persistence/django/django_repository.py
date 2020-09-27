# -*- coding: utf8 -*-

from src.shared.domain.repository import AbstractRepository

from django.db.models import Model


class DjangoRepository(AbstractRepository):
    model = Model

    def add(self, entity):
        pass

    def edit(self, entity):
        pass

    def delete(self, entity):
        pass

    def search(self, **fields):
        pass
