# -*- coding: utf-8 -*-


"""
Bus subscribers
"""

from .user_subscribers import USER_SUBSCRIBERS
from .address_subscribers import ADDRESS_SUBSCRIBERS
from .phone_subscribers import PHONE_SUBSCRIBERS
from .person_subscribers import PERSON_SUBSCRIBERS


BUS_SUBSCRIBERS = dict()
BUS_SUBSCRIBERS.update(USER_SUBSCRIBERS)
BUS_SUBSCRIBERS.update(ADDRESS_SUBSCRIBERS)
BUS_SUBSCRIBERS.update(PHONE_SUBSCRIBERS)
BUS_SUBSCRIBERS.update(PERSON_SUBSCRIBERS)
