# -*- coding: utf-8 -*-


from modules.persons.domain.entities.address import AddressFinder as GetAddressEntity
from modules.persons.domain.value_objects.person_values import (
    PersonId,
)


class GetPerson:
    """
    Name constructors to create Person
    """

    @staticmethod
    def create_person_entity(person_id: PersonId):
        """
        Create address entity
        @param address_id:
        @type address_id:
        @return:
        @rtype:
        """
        if not isinstance(person_id, PersonId):
            raise ValueError(f"Parameter person_id is not PersonId {person_id}")

        get_address_entity = GetAddressEntity(
            id=person_id
        )
        return get_address_entity
