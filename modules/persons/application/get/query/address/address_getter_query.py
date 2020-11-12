# -*- coding: utf-8 -*-


from modules.shared.domain.bus.query import Query


class AddressGetterQuery(Query):
    """
    Get Person Query
    """

    def __init__(self,
                 id: str = None):

        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self):
        raise Exception("You can't assign directly")
