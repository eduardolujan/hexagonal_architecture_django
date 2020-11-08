# -*- coding: utf-8 -*-


from modules.shared.domain.repository import UnitOfWorkEntityWrapper as AbstractUnitOfWorkEntityWrapper
from modules.shared.infrastructure.persistence.unit_of_work_entity import UnitOfWorkEntity


class DeleteUnitOfWorkEntity(AbstractUnitOfWorkEntityWrapper):
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
