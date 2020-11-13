# -*- coding: utf-8 -*-


from typing import List, NoReturn

from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.infrastructure.bus.message.in_memory import InMemoryMessageBus
from modules.shared.domain.bus.message import MessageBus
from modules.shared.domain.bus.event import EventBus, DomainEvent


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class InMemoryEventBus(EventBus):
    """
    In MemoryEventBus
    """
    def __init__(self, message_bus: MessageBus = None):
        self.suscribers = tuple()
        self.__message_bus = message_bus or InMemoryMessageBus()

    def publish(self, domain_events: List[DomainEvent]) -> NoReturn:
        """
        Publish in memory events
        @param domain_events: Domain Events
        @type domain_events: List[DomainEvent]
        @return: NoReturn
        @rtype: NoReturn
        """
        for domain_event in domain_events:
            if isinstance(domain_event, DomainEvent):
                self.__message_bus.dispatch(domain_event)
            else:
                message = f"Parameter domain_event:{domain_event} is not instance of DomainEvent"
                self.log.error(message)
                raise Exception(message)
