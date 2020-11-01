# -*- coding: utf-8 -*-


from src.persons.domain.entities import (
    Person as PersonEntity,
    Address as AddressEntity,
    Phone as PhoneEntity,
)
from src.persons.domain.value_objects import person_values


class CreatePerson:
    """
    Name constructors to create Person
    """

    @staticmethod
    def create_person_entity(id: str,
                             name: str,
                             last_name: str,
                             second_last_name: str,
                             address: AddressEntity = None,
                             phone: PhoneEntity = None):
        """
        Create a person entity
        @param id:
        @type id:
        @param name:
        @type name:
        @param last_name:
        @type last_name:
        @param second_last_name:
        @type second_last_name:
        @param address:
        @type address:
        @param phone:
        @type phone:
        @return:
        @rtype:
        """
        person_id = person_values.PersonId(id)
        person_name = person_values.Name(name)
        person_last_name = person_values.Name(last_name)
        person_second_last_name = person_values.SecondLastName(second_last_name)

        person_entity = PersonEntity(
            id=person_id,
            name=person_name,
            last_name=person_last_name,
            second_last_name=person_second_last_name,
            address=address,
            phone=phone
        )
        return person_entity
