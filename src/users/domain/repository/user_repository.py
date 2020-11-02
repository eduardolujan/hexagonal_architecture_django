from abc import ABC, abstractmethod


class UserRepository(ABC):
    """
    Asbtract User Repository
    """

    @abstractmethod
    def create(self, entity):
        """

        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def get(self, entity):
        """
        Get entity
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def update(self, entity):
        """
        Update entity
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def delete(self, entity):
        """
        Delete entity
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def all(self):
        raise NotImplementedError("Not implemented error")

