# -*- coding: utf-8 -*-


from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.shared.domain.repository import UnitOfWork
from src.persons.domain.services.create import CreateAddress as CreateAddressService
from src.persons.domain.repository import AddressRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class CreateAddress:
    """
    Create phone
    """
    def __init__(self,
                 user_repository: AddressRepository,
                 unit_of_work: UnitOfWork):

        self.__repository = user_repository
        self.__unit_of_work = unit_of_work

    def __call__(self,
                 address_id: str,
                 street: str,
                 interior_number: str,
                 outside_number: str,
                 zip_code: str,
                 city: str,
                 borough: str,
                 state: str,
                 country: str):

        address_entity = CreateAddressService(
            address_id,
            street,
            interior_number,
            outside_number,
            zip_code,
            city,
            borough,
            state,
            country
        )

        with self.__unit_of_work as uow:
            user_model_instance = self.__repository.create(address_entity)
            uow.session.add(user_model_instance)
            uow.commit()
