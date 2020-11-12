# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from typing import NoReturn, List

from modules.shared.domain.bus.event import DomainEvent


class MessageBus(ABC):
    """
    Abstract Message bus
    """

    @abstractmethod
    def dispatch(self, domain_events: List[DomainEvent]) -> NoReturn:
        """
        Dispatch event
        @param domain_events: Domain Event
        @type domain_events: modules.shared.domain.bus.event.DomainEvent
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented yet")
