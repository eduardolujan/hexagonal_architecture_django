

from had.app.models import AppUser
from src.users.domain.entities import AppUser as AppUserEntity
from src.users.domain.repository import UserRepository
from src.shared.infrastructure.persistence.django import DjangoRepository


class AppUserRepository(DjangoRepository, UserRepository):
    model = AppUser
    entity = AppUserEntity

    def all(self):
        return self._all_entities()
