# -*- coding: utf-8 -*-


from typing import Optional, Dict
from uuid import UUID

from modules.shared.domain.bus.event import DomainEvent
from modules.shared.domain.bus.event.domain_event import DomainEventInstance


class CreateUserDomainEvent(DomainEvent):
    """
    Create Person DomainEvent
    """

    def __init__(self,
                 id: str = None,
                 username: str = None,
                 password: str = None,
                 email: str = None):
        super(CreateUserDomainEvent, self).__init__(self.__id)
        self.__id = id
        self.__username = username
        self.__password = password
        self.__email = email


    def event_name(self):
        """
        Return event name
        @return: Event name
        @rtype: str
        """
        return 'user.created'

    @staticmethod
    def from_primitives(self,
                        aggregate_id: UUID,
                        body: dict = {},
                        event_id=Optional[UUID],
                        ocurred_on=Optional[str]) -> DomainEventInstance:
        raise NotImplementedError("Not implemented yet")

    def to_primitives(self) -> Dict:
        """
        To primitives
        @return: Primitives representation
        @rtype: Dict
        """
        domain_event = dict(
            id=self.__id,
            username=self.__username,
            password=self.__password,
            email=self.__email
        )
        return domain_event

    @property
    def id(self):
        return self.__id

    @id.setter
    def id_setter(self, value):
        raise Exception("You can't assign id directly")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name_setter(self, value):
        raise Exception("You can't assign name directly")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password_setter(self, value):
        raise Exception("You can't assign password directly")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email_setter(self, value):
        raise Exception("You can't assign email directly")

