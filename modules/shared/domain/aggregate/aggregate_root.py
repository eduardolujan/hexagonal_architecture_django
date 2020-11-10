# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from typing import List, NoReturn

from modules.shared.domain.bus.event import DomainEvent


class AggregateRoot(ABC):
    """
    Aggregate Root
    """

    __domain_events = list()

    def pull_domain_events(self) -> List[DomainEvent]:
        """
        Pull domain events
        @return: List of DomainEvents
        @rtype: List[DomainEvent]
        """
        domain_events = self.__domain_events
        self.__domain_events = []
        return domain_events

    def record(self, domain_event: DomainEvent) -> NoReturn:
        """
        Record
        @param domain_event:
        @type domain_event:
        @return:
        @rtype:
        """
        self.__domain_events.append(domain_event)

    def __setattr__(self, key, value):
        if '__domain_events' == key:
            raise ValueError(f"You can't modify the domain events directly {key}")


