from abc import ABC, abstractmethod


class Command(ABC):
    """
    Command Port Interface
    """

    def __setattr__(self, key, value):
        if not key.startswith('__'):
            raise Exception("Edit is not allowed")
