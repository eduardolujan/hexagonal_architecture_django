from abc import ABC, abstractmethod


class PhoneRepository(ABC):
    """

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

        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def update(self, entity):
        """

        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def delete(self, entity):
        """

        @param entity:
        @type entity:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def all(self):
        """

        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented error")

