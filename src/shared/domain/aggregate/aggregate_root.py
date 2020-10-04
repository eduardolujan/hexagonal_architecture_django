from abc import ABC, abstractmethod
from typing import List


class AggregateRoot:
    def __init__(self):
        self.__domain_events = list()

    def pull_domain_events(self):
        domain_events = self.__domain_events
        self.__domain_events = []
        return domain_events

    def record(self, domain_event):
        self.__domain_events.append(domain_event)

