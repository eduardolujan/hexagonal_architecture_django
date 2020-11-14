# -*- coding: utf-8 -*-


# Third Party
from mappers import Mapper, Evaluated
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor

from modules.shared.infrastructure.persistence.unit_of_work_entity import UnitOfWorkEntity


class OrmManager:
    """
    ORM manager
    """

    def __init__(self, model=None, entity=None):
        self.__entity = entity
        self.__model = model

    def __get(self, **fields):
        try:
            # Filter for get is necesary to wrap entities
            model_instance = self.__model.objects.filter(**fields)

        except Exception as err:
            model_instance = None

        return model_instance

    def __all(self):
        model_instances = self.__model.objects.all()
        return model_instances

    def __search(self):
        pass

    def __foreign(self, field, value):
        foreign_instance = None
        return foreign_instance

    def orm_get(self, **fields):
        """
        Get a new entity in db
        @param fields: fields in entity
        @type fields: dict
        @return: model_instance
        @rtype: type(model_instance)
        """
        model_instance = self.__get(**fields)
        mapper = Mapper(self.__entity, self.__model)

        @mapper.reader.entity
        def reader_entity(entity):
            return entity

        if not model_instance:
            return None

        model_instance = reader_entity(model_instance)
        return model_instance

    def orm_create(self, **fields) -> UnitOfWorkEntity:
        """
        Create a new entity in db
        @param fields: fields in entity
        @type fields: dict
        @return: model_instance
        @rtype: UnitOfWorkEntity
        """
        model_instance = self.__model()
        model = self.__model
        for field, value in fields.items():
            if hasattr(model_instance, field):
                model_field = getattr(model, field)
                if type(model_field) is ForwardManyToOneDescriptor:
                    foreign_model_instance = model_field.field.related_model(id=value)
                    setattr(model_instance, field, foreign_model_instance)
                else:
                    setattr(model_instance, field, value)
            else:
                raise ValueError('Field not found')

        wrapped_model_instance = UnitOfWorkEntity(model_instance,
                                                  UnitOfWorkEntity.options.CREATE.value)
        return wrapped_model_instance

    def orm_update(self, **fields) -> UnitOfWorkEntity:
        """
        Update a new entity in db
        @param fields: fields in entity
        @type fields: dict
        @return: model_instance
        @rtype: UnitOfWorkEntity
        """
        model_instance = self.__model()
        for field, value in fields.items():
            if hasattr(model_instance, field):
                setattr(model_instance, field, value)
            else:
                raise ValueError('Field not found')
        wrapped_model_instance = UnitOfWorkEntity(model_instance,
                                                  UnitOfWorkEntity.options.UPDATE.value)
        return wrapped_model_instance

    def orm_delete(self, **fields) -> UnitOfWorkEntity:
        """
        Delete a entity
        @param fields:
        @type fields:
        @return:
        @rtype:
        """
        try:
            model_instance = self.__model.objects.get(**fields)
            wrapped_model_instance = UnitOfWorkEntity(model_instance,
                                                      UnitOfWorkEntity.options.DELETE.value)
            return wrapped_model_instance
        except Exception as err:
            self.log.exception(f"Error in update model:{self.__model}, fields:{fields}, err:{err}")
            return None

    def orm_search(self, **fields):
        raise NotImplementedError("Not implemented yet")

    def orm_all(self):
        mapper = Mapper(self.__entity, self.__model)
        model_instances = self.__all()

        @mapper.reader.sequence
        def reader_entity(entities):
            return entities

        return reader_entity(model_instances)

