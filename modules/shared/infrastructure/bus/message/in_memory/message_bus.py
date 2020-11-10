# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from typing import NoReturn

from modules.shared.domain.bus.event import DomainEvent
from modules.shared.domain.bus.message import MessageBus


class InMemoryMessageBus(MessageBus):
    """
    Inmemory Message bus
    """

    def __init__(self, handlers=None):
        self.__handlers = handlers or tuple()

    def dispatch(self, domain_event: DomainEvent) -> NoReturn:
        """
        Dispatch
        @param domain_event: Domain Event
        @type domain_event: modules.shared.domain.bus.event.DomainEvent
        @return: NoReturn
        @rtype: NoReturn
        """
        raise NotImplementedError("Not implemented yet")
