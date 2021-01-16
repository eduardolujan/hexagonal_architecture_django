from modules.users.domain.entities import UserId as GetUserEntity
from modules.users.domain.value_objects import UserId


class UserFinderService:
    """
    Get user entity creator service
    """

    @staticmethod
    def get_user_entity(user_id: UserId):
        """
        Get user entity
        @param user_id:
        @type user_id:
        @return:
        @rtype:
        """
        get_user_entity = GetUserEntity(
            id=user_id
        )
        return get_user_entity
