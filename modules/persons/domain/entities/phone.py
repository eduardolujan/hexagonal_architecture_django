# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import Optional

from modules.shared.domain.aggregate import AggregateRoot
from modules.shared.domain.entities import Entity
from modules.persons.domain.value_objects import phone_values


@dataclass(frozen=True)
class Phone(Entity, AggregateRoot):
    """
    Person Entity
    """
    id: phone_values.PhoneID
    number: phone_values.Number
    extension = phone_values.Extension


@dataclass(frozen=True)
class GetPhone(Entity, AggregateRoot):
    """
    Person Entity
    """
    id: phone_values.PhoneID


