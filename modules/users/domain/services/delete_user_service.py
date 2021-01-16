

from modules.users.domain import value_objects
from modules.users.domain.entities import UserId


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

        app_user_id = value_objects.UserId(id)
        delete_user = UserId(
            id=app_user_id,
        )
        return delete_user



