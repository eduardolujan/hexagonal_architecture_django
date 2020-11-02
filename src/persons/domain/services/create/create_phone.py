# -*- coding: utf-8 -*-


from src.persons.domain.entities import (
    Phone as PhoneEntity,
)
from src.persons.domain.value_objects import phone_values


class CreatePhone:
    """
    Name constructors to create Person
    """

    @staticmethod
    def create_phone_entity(phone_id: str,
                            number: str,
                            extension: str):
        """
        Create Phone Entity
        @param phone_id: Phone ID UUID
        @type phone_id: str
        @param number: Phone Number
        @type number: str
        @param extension: Phone Extension
        @type extension: str
        @return: Phone instance
        @rtype: src.persons.domain.entities.Phone
        """
        phone_id = phone_values.PhoneID(phone_id)
        phone_number = phone_values.Number(number)
        phone_extension = phone_values.Extension(extension)

        phone_entity = PhoneEntity(
            id=phone_id,
            number=phone_number,
            extension=phone_extension
        )

        return phone_entity
