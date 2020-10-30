

from uuid import UUID

from src.shared.domain.passwords import PasswordGenerator
from src.users.domain.entities import DeleteUser as DeleteUserEntity
from src.users.domain.value_objects import UserId, Username, UserPassword, UserEmail


class DeleteUser:
    """
    Name constructors to delete User
    """

    @staticmethod
    def get_entity_by_id(id: str):
        """
        Gets DeleteUser entity
        @param id:
        @type id:
        @return:
        @rtype:
        """
        if type(id) is not str:
            raise ValueError("Not assigned password_generator")

        app_user_id = UserId(id)
        delete_user = DeleteUserEntity(
            id=app_user_id,
        )
        return delete_user



