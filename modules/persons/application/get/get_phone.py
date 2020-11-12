# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.bus.query import Query
from modules.persons.domain.repository import PhoneRepository
from modules.persons.domain.services.get import GetPhone as GetPhoneService
from modules.persons.domain.value_objects.phone_values import (
    PhoneID
)


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class PhoneGetter:
    """
    Phone Getter
    """

    def __init__(self, phone_repository: PhoneRepository):
        self.__repository = phone_repository

    def __call__(self, get_phone_query: Query):
        phone_id = PhoneID(get_phone_query.id)
        get_phone_entity = GetPhoneService.create_phone_entity(phone_id)
        phone_entity = self.__repository.get(get_phone_entity)
        return phone_entity




