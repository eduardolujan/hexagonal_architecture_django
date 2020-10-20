# -*- coding: utf-8 -*-


from django.http.request import HttpRequest

from src.shared.domain.requests.django import Request


class DjangoRequest(Request):
    def __init__(self, request: HttpRequest):
        self.request = request

    def get_body(self):
        data = self.request.data
        return data

    @property
    def request(self):
        return self.request

    @request.setter
    def request(self, value):
        raise ValueError("You don't be allowed to set this value")
