

from uuid import UUID

from src.shared.domain.passwords import PasswordGenerator
from src.users.domain.entities import DeleteUser
from src.users.domain.value_objects import UserId, Username, UserPassword, UserEmail


class DeleteUser:
    """
    Name constructors to delete User
    """
    @staticmethod
    def get_entity_by_id(id: str):

        if type(id) is not str:
            raise ValueError("Not assigned password_generator")

        app_user_id = UserId(id)
        delete_user = DeleteUser(
            id=app_user_id,
        )
        return delete_user



