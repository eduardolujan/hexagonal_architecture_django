# -*- coding: utf-8 -*-


from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.shared.domain.repository import UnitOfWork
from src.shared.domain.passwords import PasswordGenerator
from src.users.domain.services import CreateUser as CreateUserService
from src.users.domain.repository import UserRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UpdateUser:
    def __init__(self,
                 user_repository: UserRepository,
                 password_generator: PasswordGenerator,
                 unit_of_work: UnitOfWork):
        """
        Create User constructor
        @param user_repository: User repository instance
        @param password_generator: Password generator instance
        @param unit_of_work: AbstractUnitOfWork
        """
        self.repository = user_repository
        self.password_generator = password_generator
        self.unit_of_work = unit_of_work

    def __call__(self, id: str = None, username: str = None, password: str = None, email: str = None, **fields):
        user_entity = CreateUserService.create_base_user(
            id,
            username,
            password,
            email,
            self.password_generator
        )

        self.repository.update(user_entity)