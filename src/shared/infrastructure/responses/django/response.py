# -*- coding: utf-8 -*-

from rest_framework.response import Response

from src.shared.domain.responses import Response as AbstractResponse


class RestResponse(Response):
    """
    Django Rest Response
    """
    def __init__(self, response: Response = None):
        """
        Constructor
        @param response:
        @type response:
        """
        self.response = response or Response

    def __call__(self, *args, **kwargs) -> Response:
        """
        Functional magic method call
        @param args: *args
        @type args: list
        @param kwargs: *kwargs
        @type kwargs: dict
        @return: Django Rest Framework response
        @rtype: est_framework.response.Response
        """
        return self.get_response(*args, **kwargs)

    def get_response(self, *args, **kwargs) -> Response:
        """
        Get response
        @param args: *args
        @type args: list
        @param kwargs: *kwargs
        @type kwargs: dict
        @return: Django Rest Framework response
        @rtype: est_framework.response.Response
        """
        return self.response(*args, **kwargs)



