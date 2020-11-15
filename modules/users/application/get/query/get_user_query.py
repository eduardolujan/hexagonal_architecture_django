# -*- coding: utf-8 -*-


from modules.shared.domain.bus.query import Query


class UserFinderQuery(Query):
    """
    Get Person Query
    """

    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self):
        raise Exception("You can't assign directly")
