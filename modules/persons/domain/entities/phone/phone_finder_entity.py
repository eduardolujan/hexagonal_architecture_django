# -*- coding: utf-8 -*-


from dataclasses import dataclass

# Domain
from modules.shared.domain.aggregate import AggregateRoot
from modules.persons.domain.value_objects import phone_values


@dataclass
class PhoneFinder(AggregateRoot):
    """
    Person Entity
    """
    id: phone_values.PhoneID
