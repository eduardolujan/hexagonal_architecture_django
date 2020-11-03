from src.shared.domain.repository import UnitOfWorkEntityWrapper as AbstractUnitOfWorkEntityWrapper
from src.shared.infrastructure.persistence.unit_of_work_entity import UnitOfWorkEntity


class UpdateUnitOfWorkEntity(AbstractUnitOfWorkEntityWrapper):
    """
    Update UoF Entity
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
