

from had.app.models import AppUser
from src.users.domain.entities import AppUser as AppUserEntity
from src.shared.infrastructure.persistence.django import DjangoRepository, DjangoOrmManager


class AppUserRepository(DjangoRepository):
    model = AppUser
    entity = AppUserEntity


