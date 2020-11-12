# -*- coding: utf-8 -*-


from modules.shared.domain.value_objects import Integer, String, Uuid


class AddressID(Uuid):
    """
    Address ID as UUID
    """
    pass


class Street(String):
    """
    Address street as String
    """
    pass


class InteriorNumber(String):
    """
    Address interior number
    """
    pass


class OutsideNumber(String):
    """
    Address exterior number
    """
    pass


class Zipcode(String):
    """
    Address zipcode
    """
    pass


class City(String):
    """
    Address city
    """
    pass


class Borough(String):
    """
    Address borough
    """
    pass


class State(String):
    """
    Address state
    """
    pass


class Country(String):
    """
    Address country
    """
    pass
