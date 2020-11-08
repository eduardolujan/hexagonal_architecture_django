# -*- coding: utf-8 -*-


from modules.persons.domain.entities import (
    Address as AddressEntity,
)
from modules.persons.domain.value_objects.address_values import (
    AddressID,
    Street,
    InteriorNumber,
    OutsideNumber,
    Zipcode,
    City,
    Borough,
    State,
    Country
)


class CreateAddress:
    """
    Name constructors to create Person
    """

    @staticmethod
    def create_address_entity(address_id: AddressID,
                              street: Street,
                              interior_number: InteriorNumber,
                              outside_number: OutsideNumber,
                              zip_code: Zipcode,
                              city: City,
                              borough: Borough,
                              state: State,
                              country: Country):
        """
        Create Adress Entity
        @param address_id: Address ID UUID
        @type address_id: src.persons.domain.value_objects.address_values.AddressID
        @param street: Street
        @type street: src.persons.domain.value_objects.address_values.Street
        @param interior_number: InteriorNumber
        @type interior_number: src.persons.domain.value_objects.address_values.InteriorNumber
        @param outside_number: OutsideNumber
        @type outside_number: src.persons.domain.value_objects.address_values.ExternalNumber
        @param zip_code: ZipCode
        @type zip_code: src.persons.domain.value_objects.address_values.ZipCode
        @param city: City
        @type city: src.persons.domain.value_objects.address_values.City
        @param borough: Borough
        @type borough: src.persons.domain.value_objects.address_values.Borough
        @param state: State
        @type state: src.persons.domain.value_objects.address_values.State
        @param country: Country
        @type country: src.persons.domain.value_objects.address_values.Country
        @return: Address Entity
        @rtype: src.persons.domain.entities.Address
        """

        address_entity = AddressEntity(
            id=address_id,
            street=street,
            interior_number=interior_number,
            outside_number=outside_number,
            zip_code=zip_code,
            city=city,
            borough=borough,
            state=state,
            country=country
        )

        return address_entity
