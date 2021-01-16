# -*- coding: utf-8 -*-


from dataclasses import dataclass

from modules.shared.domain.aggregate import AggregateRoot
from modules.users.domain import value_objects


@dataclass
class User(AggregateRoot):
    """
    User Entity
    """
    id: value_objects.UserId
    username: value_objects.Username
    password: value_objects.Password
    email: value_objects.Email


@dataclass(frozen=True)
class UserId(AggregateRoot):
    """
    User ID entity
    """
    id: value_objects.UserId
