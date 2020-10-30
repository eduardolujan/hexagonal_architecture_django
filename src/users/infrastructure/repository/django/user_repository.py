

from had.app.models import User as AppUserModel
from src.shared.infrastructure.persistence.django import OrmManager
from src.users.domain.entities.user import User as AppUserEntity
from src.users.domain.repository import UserRepository as AbstractUserRepository


class UserRepository(OrmManager, AbstractUserRepository):

    def __init__(self, model=AppUserModel, entity=AppUserEntity):
        super(UserRepository, self).__init__(model, entity)

    def get(self, entity):
        model_instance = self.orm_get(**entity.as_dict())
        return model_instance

    def create(self, entity):
        model_instance = self.orm_create(**entity.as_dict())
        return model_instance

    def update(self, entity):
        model_instance = self.orm_create(**entity.as_dict())
        return model_instance

    def delete(self, entity):
        return self.orm_delete(**entity.as_dict())

    def all(self):
        return self.orm_all()

