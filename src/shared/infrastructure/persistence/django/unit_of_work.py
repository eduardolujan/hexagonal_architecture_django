# -*- coding: utf8 -*-


from django.db import transaction

from src.shared.domain.repository import UnitOfWork as AbstractUnitOfWork
from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from .session_uow import SessionUnitOfWork


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UnitOfWork(AbstractUnitOfWork):
    def __init__(self, session=None):
        self.__entities = set()
        self.__session = session or SessionUnitOfWork(self)

    def __enter__(self):
        transaction.set_autocommit(False)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        transaction.set_autocommit(True)

    def commit(self):
        try:
            for entity in self.__entities:
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
        if type(self.__entities) is tuple:
            raise ValueError(f"self.__entities is not tuple")
        self.__entities.add(entity)

    def update(self, entity):
        if type(self.__entities) is tuple:
            raise ValueError(f"self.__entities is not tuple")
        self.__entities.add(entity)

    def flush(self):
        self.__entities = set()

    @property
    def session(self):
        """
        Session instance
        @return: Session instance
        @rtype: AbstractSessionUnitOfWork implementation instance
        """
        return self.__session

    @session.setter
    def session(self, value):
        raise Exception("Not allowed to set this value")
