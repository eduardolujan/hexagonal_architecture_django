# -*- coding: utf-8 -*-


from typing import NoReturn

from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.bus.command import Command
from modules.shared.domain.bus.message import MessageBus
from modules.shared.domain.repository import UnitOfWork
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
                 unit_of_work: UnitOfWork,
                 message_bus: MessageBus):
        """
        Phone Creator
        @param phone_repository: Phone repository
        @type phone_repository: modules.persons.domain.repository.PhoneRepository
        @param unit_of_work: Unit of work
        @type unit_of_work: modules.shared.domain.repository.PhoneRepository
        @param message_bus:
        @type message_bus:
        """
        self.__repository = phone_repository
        self.__unit_of_work = unit_of_work
        self.__bus = message_bus

    def __call__(self, create_phone_command: Command) -> NoReturn:
        """
        Phone Creator __call__ -> functional_call(command)
        @param create_phone_command: Create phone command
        @type create_phone_command: modules.shared.domain.bus.command.Command
        @return: No Return
        @rtype: NoReturn
        """
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
