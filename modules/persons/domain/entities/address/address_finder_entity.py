# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import Optional

from modules.shared.domain.entities import Entity
from modules.persons.domain.value_objects import address_values


@dataclass
class AddressFinder(Entity):
    """
    Address Entity
    """
    id: address_values.AddressID
