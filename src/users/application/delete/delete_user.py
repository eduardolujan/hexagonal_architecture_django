# -*- coding: utf-8 -*-


from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.shared.domain.repository import UnitOfWork
from src.shared.domain.passwords import PasswordGenerator
from src.users.domain.services import CreateUser as CreateUserService
from src.users.domain.repository import UserRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class DeleteUser:
    def __init__(self, user_repository: UserRepository):
        """
        Delete User constructor
        @param user_repository: User repository instance
        """
        self.repository = user_repository

    def __call__(self, id: str = None):
        delete_entity = None
        self.repository.delete(delete_entity)

