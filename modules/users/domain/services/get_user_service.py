from uuid import UUID

from modules.users.domain.entities import GetUser as GetUserEntity
from modules.users.domain.value_objects import UserId


class GetUserService:
    """
    Get user entity creator service
    """

    @staticmethod
    def get_user_entity(user_id: UserId):
        """
        Get user entity
        @param id:
        @type id:
        @return:
        @rtype:
        """
        get_user_entity = GetUserEntity(
            id=user_id
        )
        return get_user_entity
