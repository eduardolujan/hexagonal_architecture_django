# -*- coding: utf-8 -*-

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import List, NoReturn

from .utils import UUIDEncoder
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

    def as_str(self):
        """
        Entity as str
        """
        _dict = asdict(self)
        parsed_dict = json.dumps(_dict, cls=UUIDEncoder)
        return parsed_dict

    def as_dict(self):
        """
        Entity as dict
        """
        parsed_dict = json.loads(self.as_str())
        return parsed_dict

    def __repr__(self):
        return self.as_dict()

