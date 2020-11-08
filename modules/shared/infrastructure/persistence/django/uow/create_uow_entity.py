# -*- coding: utf-8 -*-


from modules.shared.domain.repository import UnitOfWorkEntityWrapper as AbstractUnitOfWorkEntity
from modules.shared.infrastructure.persistence.unit_of_work_entity import UnitOfWorkEntity


class CreateUnitOfWorkEntity(AbstractUnitOfWorkEntity):
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
