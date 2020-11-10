# -*- coding: utf-8 -*-


from modules.persons.domain.entities import (
    GetAddress as GetAddressEntity,
)
from modules.persons.domain.value_objects.address_values import (
    AddressID,
)


class GetAddress:
    """
    Name constructors to create Person
    """

    @staticmethod
    def create_address_entity(address_id: AddressID):
        """
        Create address entity
        @param address_id:
        @type address_id:
        @return:
        @rtype:
        """
        get_address_entity = GetAddressEntity(
            id=address_id
        )
        return get_address_entity
