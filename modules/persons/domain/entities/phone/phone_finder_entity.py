# -*- coding: utf-8 -*-


from dataclasses import dataclass

# Domain
from modules.shared.domain.entities import Entity
from modules.persons.domain.value_objects import phone_values


@dataclass
class PhoneFinder(Entity):
    """
    Person Entity
    """
    id: phone_values.PhoneID
