# -*- coding: utf-8 -*-


from uuid import UUID

from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.users.domain.repository import UserRepository
from modules.shared.domain.bus.query import Query
from modules.persons.domain.services.get import GetPerson as GetPersonService
from modules.persons.domain.value_objects.person_values import (
    PersonId
)


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class PersonGetter:
    """
    Person Getter
    """

    def __init__(self, person_repository: UserRepository):
        """
        Get user service by id uuid v4
        @param person_repository:
        """
        self.__repository = person_repository

    def __call__(self, get_person_query: Query):
        person_id = PersonId(get_person_query.id)
        get_person_entity = GetPersonService.create_person_entity(person_id)
        person_entity = self.__repository.get(get_person_entity)
        return person_entity




