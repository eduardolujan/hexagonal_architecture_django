# -*- coding: utf8 -*-

import os
import sys
import inspect

from django.db import transaction

from src.shared.domain.repository import AbstractUnitOfWork, AbstractRepository
from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService


@LoggerDecorator(logger=PyLoggerService(__file__))
class DjangoUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.entities = set()
        self.save_point = None

    def __enter__(self):
        transaction.set_autocommit(False)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        transaction.set_autocommit(True)

    def commit(self):

        try:
            for entity in self.entities:
                entity.save()

        except Exception as err:
            self.rollback()

        else:
            transaction.commit()

        finally:
            self.log.info(f"Finished transaction")

    def rollback(self):
        transaction.rollback()

    def add(self, entity):
        self.entities.add(entity)

    def flush(self):
        self.entities = set()
