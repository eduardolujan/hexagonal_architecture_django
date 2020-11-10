# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from typing import NoReturn

from modules.shared.domain.bus.event import DomainEvent


class MessageBus(ABC):
    """
    Abstract Message bus
    """

    @abstractmethod
    def dispatch(self, domain_event: DomainEvent) -> NoReturn:
        """
        Dispatch event
        @param domain_event: Domain Event
        @type domain_event: modules.shared.domain.bus.event.DomainEvent
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented yet")
