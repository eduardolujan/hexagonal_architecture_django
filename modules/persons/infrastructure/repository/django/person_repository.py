# -*- coding: utf-8 -*-


from had.app.models import Person as PersonModel
from modules.shared.infrastructure.persistence.django import OrmManager
from modules.persons.domain.entities.person.person_entity import Person as PersonEntity
from modules.persons.domain.repository import PersonRepository as AbstractPersonRepository


class PersonRepository(OrmManager, AbstractPersonRepository):
    """
    Person Repository
    """

    def __init__(self, model=PersonModel, entity=PersonEntity):
        super(PersonRepository, self).__init__(model, entity)

    def get(self, entity):
        """
        Get person
        @param entity: Get entity
        @type entity: Dataclass Entity
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        model_instance = self.orm_get(**entity.as_dict())
        return model_instance

    def create(self, entity):
        """
        Create person
        @param entity:
        @type entity:
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        model_instance = self.orm_create(**entity.as_dict())
        return model_instance

    def update(self, entity):
        """
        Update person
        @param entity:
        @type entity:
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        model_instance = self.orm_create(**entity.as_dict())
        return model_instance

    def delete(self, entity):
        """
        Delete person
        @param entity:
        @type entity:
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        return self.orm_delete(**entity.as_dict())

    def all(self):
        """
        All person
        @param entity:
        @type entity:
        @return: Model Instance (self.__model)
        @rtype: Model
        """
        return self.orm_all()

