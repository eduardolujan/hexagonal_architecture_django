# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.users.domain.services import DeleteUser as DeleteUserService
from modules.users.domain.repository import UserRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UserDeleter:
    """
    Delete User
    """
    def __init__(self, user_repository: UserRepository):
        """
        Delete User constructor
        @param user_repository: User repository instance
        """
        self.repository = user_repository

    def __call__(self, id: str = None) -> None:
        """
        Delete User call
        @param id: user id entity
        @type id: int
        @return: None
        """
        delete_user_entity = DeleteUserService.get_entity_by_id(id)
        self.repository.delete(delete_user_entity)

