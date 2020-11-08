# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.bus.query import Query
from modules.persons.domain.repository import AddressRepository as AbstractAddressRepository
from modules.persons.domain.services.get import GetAddress as GetAddressService
from modules.persons.domain.value_objects.person_values import (
    PersonId
)


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class AddressGetter:
    """
    Address Getter
    """

    def __init__(self, address_repository: AbstractAddressRepository):
        """

        @param address_repository:
        @type address_repository:
        """
        self.__repository = address_repository

    def __call__(self, get_address_query: Query):
        address_id = PersonId(get_address_query.id)
        get_address_entity = GetAddressService.create_person_entity(address_id)
        address_entity = self.__repository.get(get_address_entity)
        return address_entity




