# -*- coding: utf-8 -*-


from src.persons.domain.entities import (
    Phone as PhoneEntity,
)
from src.persons.domain.value_objects.phone_values import (
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
        """
        Create Phone Entity
        @param phone_id: Phone UUID
        @type phone_id: src.persons.domain.value_objects.phone_values.PhoneID
        @param number: Phone Number
        @type number: src.persons.domain.value_objects.phone_values.Number
        @param extension: Phone Extension
        @type extension: src.persons.domain.value_objects.phone_values.Extension
        @return: Phone Entity
        @rtype: src.persons.domain.entities.Phone
        """

        phone_entity = PhoneEntity(
            id=phone_id,
            number=number,
            extension=extension
        )

        return phone_entity
