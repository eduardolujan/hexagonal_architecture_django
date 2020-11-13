# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.bus.query import Query
from modules.persons.domain.repository import AddressRepository
from modules.persons.domain.services.get import GetAddressService as GetAddressService
from modules.persons.domain.value_objects.address_values import (
    AddressID
)


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class AddressGetter:
    """
    Address Getter
    """

    def __init__(self, address_repository: AddressRepository):
        """
        Address Getter constructor
        @param address_repository:
        @type address_repository:
        """
        self.__repository = address_repository

    def __call__(self, address_getter_query: Query):
        if not isinstance(address_getter_query, Query):
            raise ValueError(f"Parameter get_address_query is not Query {address_getter_query}")

        address_id = AddressID(address_getter_query.id)
        get_address_entity = GetAddressService.create_address_entity(address_id)
        address_entity = self.__repository.get(get_address_entity)
        return address_entity




