# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService

from modules.shared.domain.bus.command import Command
from modules.shared.domain.bus.message import MessageBus
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.passwords import PasswordGenerator
from modules.persons.domain.services.create import CreatePhone as CreatePhoneService
from modules.persons.domain.repository import PhoneRepository
from modules.persons.domain.value_objects.phone_values import (
    PhoneID,
    Number,
    Extension,
)


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class PhoneCreator:
    """
    PhoneCreator
    """

    def __init__(self,
                 phone_repository: PhoneRepository,
                 password_generator: PasswordGenerator,
                 unit_of_work: UnitOfWork,
                 message_bus: MessageBus):
        """
        Create User constructor
        @param phone_repository: Phone repository instance
        @param password_generator: Password generator instance
        @param unit_of_work: AbstractUnitOfWork
        """
        self.__repository = phone_repository
        self.__password_generator = password_generator
        self.__unit_of_work = unit_of_work
        self.__bus = message_bus

    def __call__(self, create_phone_command: Command):
        phone_id = PhoneID(create_phone_command.id)
        number = Number(create_phone_command.number)
        extension = Extension(create_phone_command.extension)

        phone_number_entity = CreatePhoneService.create_phone_entity(
            phone_id,
            number,
            extension
        )

        with self.__unit_of_work as uow:
            phone_model_instance = self.__repository.create(phone_number_entity)
            uow.session.add(phone_model_instance)
            uow.commit()

        self.__bus.dispatch(phone_number_entity.pull_domain_events())
