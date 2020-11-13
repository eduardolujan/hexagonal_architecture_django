# -*- coding: utf-8 -*-


from typing import List, NoReturn
from abc import ABC, abstractmethod
# Domain
from .domain_event import DomainEvent


class EventBus(ABC):
    """
    Event bus
    """

    @abstractmethod
    def publish(self, domain_event: List[DomainEvent]) -> NoReturn:
        """
        Publish event bus
        @param domain_event:
        @type domain_event:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented yet")

