

from typing import List

from modules.shared.domain.bus.event import EventBus, DomainEvent


class InMemoryEventBus(EventBus):
    """
    In MemoryEventBus
    """
    def __init__(self):
        self.suscribers = tuple()

    def publish(self, domain_events: List[DomainEvent]) -> None:
        """
        Publish in memory events
        @param domain_events: Domain Events
        @type domain_events: List[DomainEvent]
        @return: None
        @rtype: None
        """
        for domain in domain_events:
            try:
                pass
            except Exception as err:
                pass
            finally:
                pass

