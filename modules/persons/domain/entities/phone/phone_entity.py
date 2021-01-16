# -*- coding: utf-8 -*-


from dataclasses import dataclass

from modules.shared.domain.aggregate import AggregateRoot
from modules.persons.domain.value_objects import phone_values


@dataclass
class Phone(AggregateRoot):
    """
    Person Entity
    """
    id: phone_values.PhoneID
    number: phone_values.Number
    extension: phone_values.Extension


