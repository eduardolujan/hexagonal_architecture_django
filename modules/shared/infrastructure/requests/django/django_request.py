# -*- coding: utf-8 -*-


from django.http.request import HttpRequest
from modules.shared.domain.requests import Request


class Request(Request):
    def __init__(self, request: HttpRequest):
        self.__request = request

    def get_body(self):
        data = self.__request.data
        return data

    @property
    def request(self):
        return self.__request

    @request.setter
    def request(self, value):
        raise ValueError("You don't be allowed to set this value")
