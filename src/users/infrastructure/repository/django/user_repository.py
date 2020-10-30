

from had.app.models import User as AppUserModel
from src.shared.infrastructure.persistence.django import OrmManager
from src.users.domain.entities.user import User as AppUserEntity
from src.users.domain.repository import UserRepository as AbstractUserRepository


class UserRepository(OrmManager, AbstractUserRepository):
    """
    User Repository
    """
    def __init__(self, model=AppUserModel, entity=AppUserEntity):
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

    def create(self, entity):
        """
        Create user
        @param entity:
        @type entity:
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        model_instance = self.orm_create(**entity.as_dict())
        return model_instance

    def update(self, entity):
        """
        Update user
        @param entity:
        @type entity:
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        model_instance = self.orm_create(**entity.as_dict())
        return model_instance

    def delete(self, entity):
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

