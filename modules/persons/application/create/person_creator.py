# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.passwords import PasswordGenerator
from modules.shared.domain.bus.command import Command
from modules.users.domain.services import CreateUser as CreateUserService
from modules.users.domain.repository import UserRepository



@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class PersonCreator:
    """
    Person Creator
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

    def __call__(self, create_person_command: Command):
        user_entity = CreateUserService.create_base_user(
            id,
            username,
            password,
            email,
            self.__password_generator
        )

        with self.__unit_of_work as uow:
            user_model_instance = self.__repository.create(user_entity)
            uow.session.add(user_model_instance)
            uow.commit()


