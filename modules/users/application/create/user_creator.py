# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
# Domain
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.bus.command import Command
from modules.shared.domain.passwords import PasswordGenerator
from modules.users.domain.services import CreateUserService as CreateUserService
from modules.users.domain.repository import UserRepository
from modules.users.domain.value_objects import (UserId,
                                                Username,
                                                Password,
                                                Email,)


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UserCreator:
    """
    CreateUser
    """

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
        self.__repository = user_repository
        self.__password_generator = password_generator
        self.__unit_of_work = unit_of_work

    def __call__(self, create_user_command: Command):

        user_id = UserId(create_user_command.id)
        username = Username(create_user_command.username)
        password_encripted = self.__password_generator.create(create_user_command.password)
        password = Password(password_encripted)
        email = Email(create_user_command.email)

        user_entity = CreateUserService.create_user_entity(
            id=user_id,
            username=username,
            password=password,
            email=email
        )

        with self.__unit_of_work as uow:
            user_model_instance = self.__repository.create(user_entity)
            uow.session.add(user_model_instance)
            uow.commit()
