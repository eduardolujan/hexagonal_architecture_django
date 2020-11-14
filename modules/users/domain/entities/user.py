# -*- coding: utf-8 -*-


from dataclasses import dataclass

from modules.shared.domain.entities import Entity
from modules.users.domain.value_objects import (UserId,
                                                Username,
                                                Password,
                                                Email)


@dataclass
class User(Entity):
    """
    User Entity
    """
    id: UserId
    username: Username
    password: Password
    email: Email
