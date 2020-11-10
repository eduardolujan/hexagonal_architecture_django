

from abc import ABC, abstractmethod

from .domain_event import DomainEvent


class EventBus(ABC):
    """
    Event bus
    """

    @abstractmethod
    def publish(self, domain_event: DomainEvent) -> None:
        """
        Publish event bus
        @param domain_event:
        @type domain_event:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented yet")

