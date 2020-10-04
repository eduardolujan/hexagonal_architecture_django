from abc import ABC, abstractmethod
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, TypeVar


DomainEventInstance = TypeVar('DomainEvent', bound='DomainEvent')


class DomainEvent(ABC):

    def __init__(self, aggregate_id: UUID, event_id=None, ocurred_on=None):
        """
        DomainEvent constructor
        @param aggregate_id: Agregate id as UUID v4
        @param event_id: Event id as UUID v4
        @param ocurred_on: datetime as isoformat
        """
        self.aggregate_id = aggregate_id
        self.event_id = event_id if event_id else uuid4()
        self.ocurred_on = ocurred_on if ocurred_on else datetime.now().isoformat()

    @abstractmethod
    def from_primitives(self, aggregate_id: UUID, body: dict = {}, event_id=Optional[UUID],
                        ocurred_on=Optional[str]) -> DomainEventInstance:
        """
        Create a domain event from primivites
        @param aggregate_id: Aggregate id UUID
        @param body: Payload
        @param event_id: Event id
        @param ocurred_on:
        @return: self instance
        @rtype: DomainEvent
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

    def event_id(self):
        return self.event_id

    def ocurred_on(self):
        return self.ocurred_on
