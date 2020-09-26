# -*- coding: utf8 -*-


from django.db.models import Model


class DjangoRepository:
    def __init__(self):
        self.model = Model

    def add(self, entity):
        self.model.save()

    def edit(self, entity):
        pass
