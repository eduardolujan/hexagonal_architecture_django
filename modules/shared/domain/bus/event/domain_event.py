# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, TypeVar, Dict


DomainEventInstance = TypeVar('DomainEvent', bound='DomainEvent')


class DomainEvent(ABC):
    """
    DomainEvent
    """

    def __init__(self, aggregate_id: UUID, event_id=None, ocurred_on=None):
        """
        DomainEvent constructor
        @param aggregate_id: Agregate id as UUID v4
        @param event_id: Event id as UUID v4
        @param ocurred_on: datetime as isoformat
        """
        self.__aggregate_id = aggregate_id
        self.__event_id = event_id if event_id else uuid4()
        self.__ocurred_on = ocurred_on if ocurred_on else datetime.now().isoformat()

    @abstractmethod
    def from_primitives(self,
                        aggregate_id: UUID,
                        body: dict = {},
                        event_id=Optional[UUID],
                        ocurred_on=Optional[str]) -> DomainEventInstance:

        """
        Create a domain event from primitives
        @param aggregate_id: Aggregate id UUID
        @param body: Payload
        @param event_id: Event id
        @param ocurred_on: Datetime in isoformat
        @return: self instance
        @rtype: DomainEvent
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def to_primitives(self) -> Dict:
        """
        To primitives
        @return: Primitives dict
        @rtype: Dict
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def event_name(self):
        """
        Event name
        @return: domain name
        @rtype: str
        """
        raise NotImplementedError("Not implemented yet")

    @property
    def event_id(self):
        """
        Event id
        @return:
        @rtype:
        """
        return self.__event_id

    @event_id.setter
    def event_id(self, value):
        raise Exception("You can't assign value directly")

    @property
    def ocurred_on(self):
        """
        Ocurrend_on
        @return:
        @rtype:
        """
        return self.__ocurred_on

    @ocurred_on.setter
    def ocurred_on(self):
        raise Exception("You can't assign value directly")
