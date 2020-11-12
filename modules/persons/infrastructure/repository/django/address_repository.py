# -*- coding: utf-8 -*-


from had.app.models import Address as AddressModel
from modules.shared.infrastructure.persistence.django import OrmManager
from modules.persons.domain.entities.address import Address as AddressEntity
from modules.persons.domain.repository import AddressRepository as AbstractAddressRepository


class AddressRepository(OrmManager, AbstractAddressRepository):
    """
    Person Repository
    """

    def __init__(self, model=AddressModel, entity=AddressEntity):
        """
        AddressRepository constructor
        @param model: model
        @type model: django.db.Model
        @param entity:
        @type entity:
        """
        super(AddressRepository, self).__init__(model, entity)

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

