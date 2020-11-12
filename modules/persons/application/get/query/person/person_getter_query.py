# -*- coding: utf-8 -*-


from modules.shared.domain.bus.query import Query


class PersonGetterQuery(Query):
    """
    Get Person Query
    """

    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        self.__id

    @id.setter
    def id(self):
        raise Exception("You can't assign directly")
