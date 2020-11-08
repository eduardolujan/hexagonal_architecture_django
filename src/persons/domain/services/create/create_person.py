# -*- coding: utf-8 -*-


from src.persons.domain.entities import (
    Person as PersonEntity,
    Address as AddressEntity,
    Phone as PhoneEntity,
)
from src.persons.domain.value_objects.person_values import (
    PersonId,
    Name,
    LastName,
    SecondLastName,
    Address,
    Phone
)


class CreatePerson:
    """
    Nameconstructors for Person
    """

    @staticmethod
    def create_person_entity(person_id: PersonId,
                             name: Name,
                             last_name: LastName,
                             second_last_name: SecondLastName,
                             address: Address = None,
                             phone: Phone = None):
        """

        @param person_id:
        @type person_id:
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

        person_entity = PersonEntity(
            id=person_id,
            name=name,
            last_name=last_name,
            second_last_name=second_last_name,
            address=address,
            phone=phone
        )
        return person_entity
