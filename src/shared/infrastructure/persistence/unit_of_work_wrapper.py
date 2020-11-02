from enum import Enum


class OperationOptions(Enum):
    """
    Unit of work operation options
    """
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'

    @classmethod
    def as_tuple(cls):
        """
        Get enum as tuple
        @return: Enum as tuple
        @rtype: tuple
        """
        return tuple(map(lambda c: (c.name, c.value), cls))

    @classmethod
    def as_dict(cls):
        """
        Get enum as dict
        @return: Enum as dict
        @rtype: dict
        """
        return dict(cls.as_tuple())


    @classmethod
    def as_dict_reverse(cls):
        """
        Get enum as dict reversed {key: value} -> {value: key}
        @return:
        @rtype:
        """
        enum_as_dict = cls.as_dict()
        return {v: k for k, v in enum_as_dict.items()}


class UnitOfWorkEntity:
    """
    Wrapper for unit of work
    """

    options = OperationOptions

    def __init__(self, entity_model_instance, operation_type=None):
        if operation_type not in self.options.as_dict_reverse():
            raise ValueError(f"Option not found {operation_type}")

        self.__entity_model_instance = entity_model_instance
        self.__operation_type = operation_type

    def get_entity_model(self):
        return self.__entity_model_instance

    def get_type(self):
        return self.__operation_type
