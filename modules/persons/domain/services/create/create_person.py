# -*- coding: utf-8 -*-


from typing import Optional

from modules.persons.domain.domain_events import CreatePersonDomainEvent
from modules.persons.domain.entities import Person as PersonEntity
from modules.persons.domain.value_objects.person_values import (
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
                             address: Optional[Address] = None,
                             phone: Optional[Phone] = None):

        person_entity = PersonEntity(
            id=person_id,
            name=name,
            last_name=last_name,
            second_last_name=second_last_name,
            address=address,
            phone=phone
        )

        # Create domain event
        create_person_domain_event = CreatePersonDomainEvent(id=person_id.value,
                                                             name=name.value,
                                                             last_name=last_name.value,
                                                             second_last_name=second_last_name.value,
                                                             address=address.value,
                                                             phone=phone.value)

        # Record the event in entity
        person_entity.record(create_person_domain_event)

        return person_entity
