# -*- coding: utf-8 -*-


from typing import Optional, Dict
from uuid import UUID

from modules.shared.domain.bus.event import DomainEvent
from modules.shared.domain.bus.event.domain_event import DomainEventInstance


class CreatePersonDomainEvent(DomainEvent):
    """
    Create Person DomainEvent
    """

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 last_name: str = None,
                 second_last_name: str = None,
                 address: Optional[str] = None,
                 phone: Optional[str] = None):

        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__second_last_name = second_last_name
        self.__address = address
        self.__phone = phone

    def event_name(self):
        """
        Return event name
        @return: Event name
        @rtype: str
        """
        return 'person.created'

    def from_primitives(self,
                        aggregate_id: UUID,
                        body: dict = {},
                        event_id=Optional[UUID],
                        ocurred_on=Optional[str]) -> DomainEventInstance:
        """
        From primitives
        @param aggregate_id:
        @type aggregate_id:
        @param body:
        @type body:
        @param event_id:
        @type event_id:
        @param ocurred_on:
        @type ocurred_on:
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented yet")

    def to_primitives(self) -> Dict:
        """
        To primitives
        @return: Primitives representation
        @rtype: Dict
        """
        domain_event = dict(
            id=self.__id,
            name=self.__name,
            last_name=self.__last_name,
            second_last_name=self.__second_last_name,
            address=self.__address,
            phone=self.__phone,
        )
        return domain_event

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def second_last_name(self):
        return self.__second_last_name

    @property
    def address(self):
        return self.__address
