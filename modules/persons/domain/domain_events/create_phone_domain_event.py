
from typing import Optional, Dict
from uuid import UUID

from modules.shared.domain.bus.event import DomainEvent
from modules.shared.domain.bus.event.domain_event import DomainEventInstance


class CreatePhoneDomainEvent(DomainEvent):
    """
    Create Phone DomainEvent
    """

    def __init__(self,
                 id: str,
                 number: str,
                 extension: str):
        """
        Constructor CreatePhoneDomainEvent
        @param id: Phone ID
        @type id: str
        @param number: Phone number
        @type number: str
        @param extension: Phone extension
        @type extension: str
        """
        self.__id = id
        self.__number = number
        self.__extension = extension

    def event_name(self):
        """
        Return event name
        @return: Event name
        @rtype: str
        """
        return 'phone.created'

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
            number=self.__number,
            extension=self.__extension
        )
        return domain_event

    @property
    def id(self):
        return self.__id

    @property
    def number(self):
        return self.__number

    @property
    def extension(self):
        return self.__extension

