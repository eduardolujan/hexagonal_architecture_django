# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import Optional

from modules.shared.domain.aggregate import AggregateRoot
from modules.shared.domain.entities import Entity
from modules.persons.domain.value_objects import address_values


@dataclass
class Address(Entity):
    """
    Address Entity
    """
    id: address_values.AddressID
    street: address_values.Street
    interior_number: address_values.InteriorNumber
    outside_number: address_values.OutsideNumber
    zip_code: address_values.Zipcode
    city: address_values.City
    borough: address_values.Borough
    state: address_values.State
    country: address_values.Country

