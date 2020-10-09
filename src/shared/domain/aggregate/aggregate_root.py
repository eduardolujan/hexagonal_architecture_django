from abc import ABC, abstractmethod
from typing import List


class AggregateRoot(ABC):
    __domain_events = list()

    def pull_domain_events(self):
        domain_events = self.__domain_events
        self.__domain_events = []
        return domain_events

    def record(self, domain_event):
        self.__domain_events.append(domain_event)

    def __setattr__(self, key, value):
        if '__domain_events' == key:
            raise ValueError("You can't modify the domain events directly")


