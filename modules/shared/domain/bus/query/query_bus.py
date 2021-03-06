# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod

from .query import Query
from .response import Response


class QueryBus(ABC):
    """
    Query Bus
    """

    @abstractmethod
    def ask(self, query: Query) -> Response:
        """
        QueryBus Ask
        @param query: query
        @type query: Query
        @return: Response
        @rtype: Response
        """
        raise NotImplementedError("Not implemented yet")
