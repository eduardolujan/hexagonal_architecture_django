# -*- coding: utf-8 -*-


from modules.persons.domain.domain_events import CreatePhoneDomainEvent
from modules.persons.domain.entities.phone import Phone as PhoneEntity
from modules.persons.domain.value_objects.phone_values import (
    PhoneID,
    Number,
    Extension
)


class CreatePhone:
    """
    Name constructors to create Person
    """

    @staticmethod
    def create_phone_entity(phone_id: PhoneID,
                            number: Number,
                            extension: Extension):

        # Create entity
        phone_entity = PhoneEntity(
            id=phone_id,
            number=number,
            extension=extension)

        # Create domain event
        create_phone_domain_event = CreatePhoneDomainEvent(
            id=phone_id.value,
            number=number.value,
            extension=extension.value)

        # Record the event in entity
        phone_entity.record(create_phone_domain_event)

        return phone_entity
