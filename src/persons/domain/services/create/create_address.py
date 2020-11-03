# -*- coding: utf-8 -*-


from src.persons.domain.entities import (
    Address as AddressEntity,
)
from src.persons.domain.value_objects import address_values


class CreateAddress:
    """
    Name constructors to create Person
    """

    @staticmethod
    def create_address_entity(address_id: str,
                              street: str,
                              interior_number: str,
                              outside_number: str,
                              zip_code: str,
                              city: str,
                              borough: str,
                              state: str,
                              country: str):

        address_id = address_values.AddressID(address_id)
        address_street = address_values.Street(street)
        address_interior_number = address_values.InteriorNumber(interior_number)
        address_outside_number = address_values.OutsideNumber(outside_number)
        address_zip_code = address_values.Zipcode(zip_code)
        address_city = address_values.City(city)
        address_borough = address_values.Borough(borough)
        address_state = address_values.State(state)
        address_country = address_values.Country(country)

        address_entity = AddressEntity(
            id=address_id,
            street=address_street,
            interior_number=address_interior_number,
            outside_number=address_outside_number,
            zip_code=address_zip_code,
            city=address_city,
            borough=address_borough,
            state=address_state,
            country=address_country
        )

        return address_entity
