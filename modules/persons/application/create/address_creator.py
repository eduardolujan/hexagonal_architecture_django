# -*- coding: utf-8 -*-

from typing import NoReturn

from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.bus.message import MessageBus
from modules.shared.domain.bus.command import Command
from modules.persons.domain.services.create import CreateAddress as CreateAddressService
from modules.persons.domain.repository import AddressRepository
from modules.persons.domain.value_objects.address_values import (
    AddressID,
    Street,
    InteriorNumber,
    OutsideNumber,
    Zipcode,
    City,
    Borough,
    State,
    Country
)


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class AddressCreator:
    """
    Create phone
    """
    def __init__(self,
                 address_repository: AddressRepository,
                 unit_of_work: UnitOfWork,
                 message_bus: MessageBus):

        self.__repository = address_repository
        self.__unit_of_work = unit_of_work
        self.__bus = message_bus
        pass

    def __call__(self, create_address_command: Command) -> NoReturn:
        """
        Create address
        @param create_address_command: Command
        @type create_address_command: modules.shared.domain.bus.command.Command
        @return: No Return
        @rtype: NoReturn
        """

        address_id = AddressID(create_address_command.id)
        street = Street(create_address_command.street)
        interior_number = InteriorNumber(create_address_command.interior_number)
        outside_number = OutsideNumber(create_address_command.outside_number)
        zip_code = Zipcode(create_address_command.zip_code)
        city = City(create_address_command.city)
        borough = Borough(create_address_command.borough)
        state = State(create_address_command.outside_number)
        country = Country(create_address_command.outside_number)

        address_entity = CreateAddressService.create_address_entity(
            address_id,
            street,
            interior_number,
            outside_number,
            zip_code,
            city,
            borough,
            state,
            country)

        with self.__unit_of_work as uow:
            user_model_instance = self.__repository.create(address_entity)
            uow.session.add(user_model_instance)
            uow.commit()

        self.__bus.dispatch(address_entity.pull_domain_events())

