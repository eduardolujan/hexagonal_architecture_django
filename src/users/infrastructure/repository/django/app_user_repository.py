

from had.app.models import AppUser as AppUserModel
from src.shared.infrastructure.persistence.django import DjangoOrmManager
from src.users.domain.entities.app_user import AppUser as AppUserEntity
from src.users.domain.repository import UserRepository


class UserRepository(DjangoOrmManager, UserRepository):

    def __init__(self, model=AppUserModel, entity=AppUserEntity):
        super(UserRepository, self).__init__(model, entity)

    def create(self, entity: AppUserEntity):
        model_instance = self.orm_create(**entity.as_dict())
        return model_instance

    def all(self):
        return self.orm_all()

