# -*- coding: utf-8 -*-


from src.shared.domain.value_objects import Integer, String, Uuid


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


class InteriorNumber(Integer):
    """
    Address interior number
    """
    pass


class OutsideNumber(Integer):
    """
    Address exterior number
    """
    pass


class Zipcode(Integer):
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
