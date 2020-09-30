

from had.app.models import AppUser
from src.shared.infrastructure.persistence.django import DjangoRepository


class AppUserRepository(DjangoRepository):
    model = AppUser

