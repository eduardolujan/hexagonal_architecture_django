# -*- coding: utf8 -*-

import os
import sys
import inspect

from django.db import transaction
from .django_repository import DjangoRepository

from src.shared.domain.repository import AbstractUnitOfWork, AbstractRepository
from src.shared.infrastructure.logs import LoggerDecorator, PyLoggerService


@LoggerDecorator(logger=PyLoggerService(__file__))
class DjangoUnitOfWork(AbstractUnitOfWork):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def __enter__(self):
        transaction.set_autocommit(False)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        transaction.set_autocommit(True)

    def commit(self):
        try:
            for entity in self.repository.entities:
                entity.save()
        except Exception as err:
            self.log.exception(f"Error in {__class__}::{inspect.currentframe().f_code.co_name}")
            transaction.rollback()
        else:
            # @TODO: Add logs
            transaction.commit()

    def rollback(self):
        transaction.rollback()
