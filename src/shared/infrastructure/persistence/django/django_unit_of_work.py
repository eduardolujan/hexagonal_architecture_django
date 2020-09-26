# -*- coding: utf8 -*-


from django.db import transaction

from .django_repository import DjangoRepository
from src.shared.domain.repository import AbstractUnitOfWork


class DjangoUnitOfWork(AbstractUnitOfWork):

    def __enter__(self):
        self.batches = DjangoRepository()
        transaction.set_autocommit(False)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        transaction.set_autocommit(True)

    def commit(self):
        for batch in self.batches.seen:
            self.batches.update(batch)
        transaction.commit()

    def rollback(self):
        transaction.rollback()
