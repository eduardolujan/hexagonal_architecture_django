# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from typing import NoReturn, List

from .bus_suscribers import BUS_SUBSCRIBERS
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.bus.event import DomainEvent
from modules.shared.domain.bus.message import MessageBus


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class InMemoryMessageBus(MessageBus):
    """
    Inmemory Message bus
    """

    def __init__(self, handlers=None):
        self.__handlers = handlers or BUS_SUBSCRIBERS

    def dispatch(self, domain_event: DomainEvent) -> NoReturn:
        """
        Dispatch
        @param domain_event: DomainEvent
        @type domain_event: modules.shared.domain.bus.event.DomainEvent
        @return: NoReturn
        @rtype: NoReturn
        """
        handlers = self.__handlers.get(domain_event.__class__.__name__)
        map(lambda handler: handler(domain_event), handlers)
