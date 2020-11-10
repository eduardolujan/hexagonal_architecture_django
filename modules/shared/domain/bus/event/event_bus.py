# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from typing import NoReturn

from .domain_event import DomainEvent


class EventBus(ABC):
    """
    Event bus
    """

    @abstractmethod
    def publish(self, domain_event: DomainEvent) -> NoReturn:
        """
        Publish event bus
        @param domain_event:
        @type domain_event:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented yet")

