import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from functools import wraps
from typing import Optional, Iterator, Generator, NoReturn, get_type_hints
from django.db.models import Model
from django.db.models.query import QuerySet

from had.app.models import User as UserModel
from modules.users.domain.entities import User as UserEntity
from modules.shared.domain.entities import Entity


class ModelMapper:
    """
    Model Mapper
    """

    def __init__(self, model_instance, model, entity):
        self.__model_instance = model_instance
        self.__model = model
        self.__entity = entity

    def __get_field_name(self, field):
        """
        Get field name
        @param field:
        @type field:
        @return:
        @rtype:
        """
        return field.name
        attname = getattr(field, "attname", None)
        if attname is not None and field.name != attname:
            return attname

    def get_entity(self, model_instance):
        fields = self.__model._meta.get_fields()
        model_field_names = [self.__get_field_name(field) for field in fields
                             if hasattr(model_instance, self.__get_field_name(field))]

        entity_fields = get_type_hints(self.__entity)
        entity_data = {
            entity_field: getattr(model_instance, entity_field)
            for entity_field in entity_fields if entity_field in model_field_names
        }
        return self.__entity(**entity_data)

    def __call__(self) -> Iterator[Entity]:
        if isinstance(self.__model_instance, QuerySet):
            return (self.get_entity(instance) for instance in self.__model_instance)
        return self.get_entity(self.__model_instance)


class ModelEntityMapper:
    """
    Mapper
    """
    def __init__(self, model: Model = None, entity: Entity = None):
        if not issubclass(model, Model):
            raise ValueError(f"Parameter model: {model} is not instance of Model")

        if not issubclass(entity, Entity):
            raise ValueError(f"Parameter model: {entity} is not instance of Entity")

        self.__model = model
        self.__entity = entity

    def __call__(self, method):
        @wraps(method)
        def mapper(*args, **kwargs):
            """
            Mapper
            @param args:
            @type args:
            @param kwargs:
            @type kwargs:
            @return:
            @rtype:
            """
            model_instance = method(*args, **kwargs)
            model_mapper = ModelMapper(model_instance, self.__model, self.__entity)
            return model_mapper()
        return mapper


class A:
    def __init__(self):
        pass

    @ModelEntityMapper(model=UserModel, entity=UserEntity)
    def method(self, test, test1=None) -> Generator[UserEntity, None, None]:
        user = UserModel.objects.all()
        return user


user_generator = A().method('test', test1='test1')
pass
