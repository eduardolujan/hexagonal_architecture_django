

from had.app.models import User as UserModel
from src.shared.infrastructure.persistence.django import OrmManager
from src.shared.infrastructure.persistence.unit_of_work_entity import UnitOfWorkEntity
from src.users.domain.entities.user import User as AppEntity
from src.users.domain.repository import UserRepository as AbstractUserRepository


class UserRepository(OrmManager, AbstractUserRepository):
    """
    User Repository
    """

    def __init__(self, model=UserModel, entity=AppEntity):
        super(UserRepository, self).__init__(model, entity)

    def get(self, entity):
        """
        Get user
        @param entity: Get entity
        @type entity: Dataclass Entity
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        model_instance = self.orm_get(**entity.as_dict())
        return model_instance

    def create(self, entity) -> UnitOfWorkEntity:
        """
        Create user
        @param entity:
        @type entity:
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        model_instance = self.orm_create(**entity.as_dict())
        return model_instance

    def update(self, entity) -> UnitOfWorkEntity:
        """
        Update user
        @param entity:
        @type entity:
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        model_instance = self.orm_create(**entity.as_dict())
        return model_instance

    def delete(self, entity) -> UnitOfWorkEntity:
        """
        Delete user
        @param entity:
        @type entity:
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        return self.orm_delete(**entity.as_dict())

    def all(self):
        """
        All user
        @param entity:
        @type entity:
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        return self.orm_all()

