# -*- coding: utf-8 -*-


from src.shared.domain.value_objects import Integer, String, Uuid


class PhoneID(Uuid):
    """
    Phone ID
    """
    pass


class Number(String):
    """
    Phone number
    """
    pass


class Extension(String):
    """
    Extension
    """
