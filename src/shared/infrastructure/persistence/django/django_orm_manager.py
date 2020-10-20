
from mappers import Mapper, Evaluated


class DjangoOrmManager:

    def __init__(self, model=None, entity=None):
        self.entity = entity
        self.model = model

    def __get(self, **fields):
        try:
            model_instance = self.model.objects.filter(**fields)
        except Exception as err:
            model_instance = None
        return model_instance

    def __all(self):
        model_instances = self.model.objects.all()
        return model_instances

    def __search(self):
        pass

    def orm_get(self, **fields):
        model_instance = self.__get(**fields)
        mapper = Mapper(self.entity, self.model)

        @mapper.reader.entity
        def reader_entity(entity):
            return entity

        if not model_instance:
            return None

        model_instance = reader_entity(model_instance)
        return model_instance

    def orm_create(self, **fields):
        model_instance = self.model()
        for field, value in fields.items():
            if hasattr(model_instance, field):
                setattr(model_instance, field, value)
            else:
                raise ValueError('Field not found')
        return model_instance

    def orm_update(self, **fields):
        model_instance = self.model()
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
        mapper = Mapper(self.entity, self.model)
        model_instances = self.__all()

        @mapper.reader.sequence
        def reader_entity(entities):
            return entities

        return reader_entity(model_instances)

