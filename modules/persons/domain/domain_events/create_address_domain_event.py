# -*- coding: utf-8 -*-


from typing import Optional, Dict
from uuid import UUID

from modules.shared.domain.bus.event import DomainEvent
from modules.shared.domain.bus.event.domain_event import DomainEventInstance


class CreateAddressDomainEvent(DomainEvent):
    """
    Create Address DomainEvent
    """

    def __init__(self,
                 id: str = None,
                 street: str = None,
                 interior_number: str = None,
                 outside_number: str = None,
                 zip_code: str = None,
                 city: str = None,
                 borough: str = None,
                 state: str = None,
                 country: str = None):

        super(CreateAddressDomainEvent, self).__init__(id)
        self.__id = id
        self.__street = street
        self.__interior_number = interior_number
        self.__outside_number = outside_number
        self.__zip_code = zip_code
        self.__city = city
        self.__borough = borough
        self.__state = state
        self.__country = country


    def event_name(self):
        """
        Return event name
        @return: Event name
        @rtype: str
        """
        return 'address.created'

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
            street=self.__street,
            interior_number=self.__interior_number,
            outside_number=self.__outside_number,
            zip_code=self.__zip_code,
            city=self.__city,
            borough=self.__borough,
            state=self.__state,
            country=self.__country
        )
        return domain_event

    @property
    def id(self):
        return self.__id

    @property
    def street(self):
        return self.__street

    @property
    def interior_number(self):
        return self.__street

    @property
    def outside_number(self):
        return self.__outside_number

    @property
    def zip_code(self):
        return self.__zip_code

    @property
    def city(self):
        return self.__city

    @property
    def borough(self):
        return self.__borough

    @property
    def state(self):
        return self.__state

    @property
    def country(self):
        return self.__country
