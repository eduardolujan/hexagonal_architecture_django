# -*- coding: utf-8 -*-


from mappers import Mapper, Evaluated


class OrmManager:

    def __init__(self, model=None, entity=None):
        self.__entity = entity
        self.__model = model

    def __get(self, **fields):
        try:
            model_instance = self.__model.objects.filter(**fields)
        except Exception as err:
            model_instance = None
        return model_instance

    def __all(self):
        model_instances = self.__model.objects.all()
        return model_instances

    def __search(self):
        pass

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

    def orm_create(self, **fields):
        """
        Create a new entity in db
        @param fields: fields in entity
        @type fields: dict
        @return: model_instance
        @rtype: type(self.model)
        """
        model_instance = self.__model()
        for field, value in fields.items():
            if hasattr(model_instance, field):
                setattr(model_instance, field, value)
            else:
                raise ValueError('Field not found')

        return model_instance

    def orm_update(self, **fields):
        """
        Create a new entity in db
        @param fields: fields in entity
        @type fields: dict
        @return: model_instance
        @rtype: type(model_instance)
        """
        model_instance = self.__model()
        for field, value in fields.items():
            if hasattr(model_instance, field):
                setattr(model_instance, field, value)
            else:
                raise ValueError('Field not found')
        return model_instance

    def orm_delete(self, **fields):
        raise NotImplementedError("Not implemented yet")

    def orm_search(self, **fields):
        raise NotImplementedError("Not implemented yet")

    def orm_all(self):
        mapper = Mapper(self.__entity, self.__model)
        model_instances = self.__all()

        @mapper.reader.sequence
        def reader_entity(entities):
            return entities

        return reader_entity(model_instances)

