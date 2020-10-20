from uuid import UUID

from src.users.domain.entities import GetUser as GetUserEntity
from src.users.domain.value_objects import UserId


class GetUser:
    @staticmethod
    def get_user_by_id(id: UUID):
        get_user_entity = GetUserEntity(
            id=UserId(id)
        )
        return get_user_entity
