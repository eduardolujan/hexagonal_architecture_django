# -*- coding: utf-8 -*-


from src.shared.domain.entities import Entity
from src.persons.domain.value_objects import phone_values


class Phone(Entity):
    """
    Person Entity
    """
    id: phone_values.PhoneID
    number: phone_values.Number
    extension = phone_values.Extension


