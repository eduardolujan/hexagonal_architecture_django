# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import Optional

from modules.shared.domain.entities import Entity
from modules.persons.domain.value_objects import person_values


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


@dataclass(frozen=True)
class GetPerson(Entity):
    """
    Person entity
    """
    id: person_values.PersonId
