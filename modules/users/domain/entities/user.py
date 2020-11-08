# -*- coding: utf-8 -*-


from dataclasses import dataclass

from modules.shared.domain.entities import Entity
from modules.users.domain.value_objects import (UserId, Username, UserPassword, UserEmail)


@dataclass(frozen=True)
class User(Entity):
    id: UserId
    username: Username
    password: UserPassword
    email: UserEmail
