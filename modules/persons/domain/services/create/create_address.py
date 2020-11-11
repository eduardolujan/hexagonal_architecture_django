# -*- coding: utf-8 -*-


from modules.persons.domain.domain_events import CreateAddressDomainEvent
from modules.persons.domain.entities import Address as AddressEntity
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

        address_entity = AddressEntity(id=address_id,
                                       street=street,
                                       interior_number=interior_number,
                                       outside_number=outside_number,
                                       zip_code=zip_code,
                                       city=city,
                                       borough=borough,
                                       state=state,
                                       country=country)

        # Create domain event
        create_address_domain_event = CreateAddressDomainEvent(
            id=address_id.value,
            street=street.value,
            interior_number=interior_number.value,
            outside_number=outside_number.value,
            zip_code=zip_code.value,
            city=city.value,
            borough=borough.value,
            state=state.value,
            country=country.value
        )

        # Record the event in entity
        address_entity.record(create_address_domain_event)

        return address_entity
