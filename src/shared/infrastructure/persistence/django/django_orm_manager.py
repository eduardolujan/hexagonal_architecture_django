
from django.db.models import Model
from mappers import Mapper, Evaluated


class DjangoOrmManager:
    def __init__(self, entity, model):
        self.entity = entity
        self.model = model

    def __get(self, **fields):
        try:
            model_instance = self.model.objects.get(**fields)
        except Exception as err:
            model_instance = None
        return model_instance

    def __all(self):
        model_instances = self.model.objects.all()
        return model_instances

    def __search(self):
        pass

    def get_orm(self, **fields):
        mapper = Mapper(self.entity, self.model)
        model_instance = self.__get(**fields)

        @mapper.reader.optional
        def reader_entity(_model_instance):
            return _model_instance

        if model_instance:
            return reader_entity(model_instance)

        return model_instance

    def orm_create(self, **fields):
        model_instance = self.model()
        for field, value in fields.items():
            if hasattr(model_instance, field):
                setattr(model_instance, field, value)
            else:
                raise Exception('Field not found')
        try:
            model_instance.save()
        except Exception as err:
            # Log this error
            raise Exception(f'Error when try to save {self.model}')

    def orm_all(self):
        mapper = Mapper(self.entity, self.model)
        model_instances = self.__all()

        @mapper.reader.iterable
        def reader_entity(entity):
            return entity

        return reader_entity(model_instances)
