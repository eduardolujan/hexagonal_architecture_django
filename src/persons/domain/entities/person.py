# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import Optional

from src.shared.domain.entities import Entity
from src.persons.domain.value_objects import person_values


@dataclass(frozen=True)
class Person(Entity):
    """
    Person entity
    """
    id: person_values.PersonId
    name: person_values.Name
    last_name: person_values.LastName
    second_last_name: person_values.SecondLastName
    address: Optional[person_values.Address]
    phone: Optional[person_values.Phone]
