


from abc import ABC, abstractmethod
from modules.shared.domain.entities import Entity


class PhoneRepository(ABC):
    """
    Phone Repository
    """

    @abstractmethod
    def get(self, entity: Entity):
        """
        Get
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def create(self, entity: Entity):
        """
        Create
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def update(self, entity: Entity):
        """
        Update
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def delete(self, entity: Entity):
        """
        Delete
        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def all(self):
        """
        All
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

