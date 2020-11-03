# -*- coding: utf8 -*-


from datetime import datetime

from django.db import transaction

from .session_uow import SessionUnitOfWork
from src.shared.domain.repository import UnitOfWork as AbstractUnitOfWork
from src.shared.infrastructure.persistence.unit_of_work_wrapper import UnitOfWorkEntity
from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService


class CreateUnitOfWorkEntity:
    """
    Create UoF Entity
    """
    def __init__(self, uof_entity: UnitOfWorkEntity):
        self.__uof_entity = uof_entity

    def execute(self):
        """
        Execute for Create UnitOfWorkEntity
        @return:
        @rtype:
        """
        model_instance = self.__uof_entity.get_entity_model()
        model_instance.save()


class UpdateUnitOfWorkEntity:
    """
    Update UoF Entity
    """
    def __init__(self, uof_entity: UnitOfWorkEntity):
        self.__uof_entity = uof_entity

    def execute(self):
        """
        Execute for Update UnitOfWorkEntity
        @return:
        @rtype:
        """
        model_instance = self.__uof_entity.get_entity_model()
        model_instance.save()


class DeleteUnitOfWorkEntity:
    """
    Delete UoF Entity
    """

    def __init__(self, uof_entity: UnitOfWorkEntity):
        self.__uof_entity = uof_entity

    def execute(self):
        """
        Execute for Delete UnitOfWorkEntity
        @return:
        @rtype:
        """
        model_instance = self.__uof_entity.get_entity_model()
        model_instance.delete()


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UnitOfWork(AbstractUnitOfWork):
    """
    Unit of Work
    """

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
                if entity.get_type() == 'create':
                    CreateUnitOfWorkEntity(entity).execute()

                elif entity.get_type() == 'update':
                    UpdateUnitOfWorkEntity(entity).execute()

                elif entity.get_type() == 'delete':
                    DeleteUnitOfWorkEntity(entity).execute()

                else:
                    raise Exception(f"Option not found {entity.get_type()}")

        except Exception as err:
            self.log.exception(f"Error in commit, err:{err}")
            self.rollback()

        else:
            transaction.commit()
            self.log.info(f"Commited transaction Date:{datetime.now()}")

        finally:
            self.log.info(f"Finished transaction Date:{datetime.now()}")

    def rollback(self):
        transaction.rollback()

    def add(self, uof_entity: UnitOfWorkEntity):
        if type(self.__entities) is tuple:
            raise ValueError(f"self.__entities is not tuple")

        if not isinstance(uof_entity, UnitOfWorkEntity):
            raise ValueError(f"{uof_entity} is not instance of UnitOfWorkEntity")

        self.__entities.add(uof_entity)

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
