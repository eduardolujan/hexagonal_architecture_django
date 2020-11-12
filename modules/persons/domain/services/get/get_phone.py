# -*- coding: utf-8 -*-


from modules.persons.domain.entities.address import GetAddress as GetAddressEntity
from modules.persons.domain.value_objects.address_values import AddressID


class GetPhone:
    """
    Nameconstructors to get Phone
    """

    @staticmethod
    def create_phone_entity(address_id: AddressID):
        get_address_entity = GetAddressEntity(
            id=address_id
        )
        return get_address_entity
