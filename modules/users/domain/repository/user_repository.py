from abc import ABC, abstractmethod


class UserRepository(ABC):
    """
    Abstract User Repository
    """

    @abstractmethod
    def create(self, entity):
        """
        Create entity
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def get(self, entity) -> object:
        """
        Get entity
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def update(self, entity) -> object:
        """
        Update entity
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def delete(self, entity) -> object:
        """
        Delete entity
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def all(self) -> object:
        """
        All entities
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

