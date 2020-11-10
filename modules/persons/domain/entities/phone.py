# -*- coding: utf-8 -*-


from dataclasses import dataclass
from modules.shared.domain.entities import Entity
from modules.persons.domain.value_objects import phone_values


@dataclass(frozen=True)
class Phone(Entity):
    """
    Person Entity
    """

    id: phone_values.PhoneID
    number: phone_values.Number
    extension = phone_values.Extension


