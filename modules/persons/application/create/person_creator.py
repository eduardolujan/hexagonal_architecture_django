# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.bus.command import Command
from modules.persons.domain.services.create import CreatePerson as CratePersonService
from modules.persons.domain.repository import PersonRepository
from modules.persons.domain.value_objects.person_values import (
    PersonId,
    Name,
    LastName,
    SecondLastName,
    Address,
    Phone
)


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class PersonCreator:
    """
    Person Creator
    """

    def __init__(self,
                 person_repository: PersonRepository,
                 unit_of_work: UnitOfWork):
        """
        Person Creator
        @param person_repository:
        @type person_repository:
        @param unit_of_work:
        @type unit_of_work:
        """
        self.__person_repository = person_repository
        self.__unit_of_work = unit_of_work

    def __call__(self, create_person_command: Command) -> None:
        """
        Create Person
        @param create_person_command: Create person command
        @type create_person_command: Command
        @return: None
        @rtype: None
        """
        person_id = PersonId(create_person_command.id)
        name = Name(create_person_command.name)
        last_name = LastName(create_person_command.last_name)
        second_last_name = SecondLastName(create_person_command.second_last_name)
        address = Address(create_person_command.address)
        phone = Phone(create_person_command.phone)

        person_entity = CratePersonService.create_person_entity(
            person_id,
            name,
            last_name,
            second_last_name,
            address,
            phone
        )

        with self.__unit_of_work as uow:
            person_model_instance = self.__person_repository.create(person_entity)
            uow.session.add(person_model_instance)
            uow.commit()




