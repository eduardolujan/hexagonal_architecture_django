# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from typing import NoReturn, List

from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.bus.event import DomainEvent
from modules.shared.domain.bus.message import MessageBus


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class InMemoryMessageBus(MessageBus):
    """
    Inmemory Message bus
    """

    def __init__(self, handlers=None):
        self.__handlers = handlers or tuple()

    def dispatch(self, domain_events: List[DomainEvent]) -> NoReturn:
        """
        Dispatch
        @param domain_events: [DomainEvent, DomainEvent, ...]
        @type domain_events: List[modules.shared.domain.bus.event.DomainEvent]
        @return: NoReturn
        @rtype: NoReturn
        """
        for domain_event in domain_events:
            self.log.info(f"Domain event {domain_event}")
