from uuid import UUID

from src.users.domain.entities import GetUser as GetUserEntity
from src.users.domain.value_objects import AppUserId


class GetUser:
    @staticmethod
    def get_user_by_id(id: UUID):
        get_user_entity = GetUserEntity(
            id=AppUserId(id)
        )
        return get_user_entity
