# -*- coding: utf-8 -*-

from rest_framework.response import Response

from src.shared.domain.responses import AbstractResponse as AbstractResponse


class RestResponse(AbstractResponse):
    def __init__(self, response: Response = None):
        self.response = response or Response

    def __call__(self, *args, **kwargs):
        return self.get_response(*args, **kwargs)

    def get_response(self, *args, **kwargs):
        return self.response(*args, **kwargs)



