
from abc import ABC, abstractmethod
import mappers


class DjangoRepository(ABC):

    def get_orm(self, **fields):
        try:
            model_instance = self.model.objects.get(**fields)
        except Exception as err:
            model_instance = None
        return model_instance

    def get_all_orm(self):
        model_instances = self.model.objects.all()
        return model_instances

    def _get_entity(self, **fields):
        mapper = mappers.Mapper(self.entity, self.model)
        model_instance = self.get_orm(**fields)

        @mapper.reader.optional
        def reader_entity(_model_instance):
            return _model_instance

        if model_instance:
            return reader_entity(model_instance)

        return model_instance

    def _create_entity(self, **fields):
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

    def _all_entities(self):
        mapper = mappers.Mapper(self.entity, self.model)
        model_instances = self.get_all_orm()

        @mapper.reader.sequence
        def reader_entity(entity):
            return entity

        return reader_entity(model_instances)
