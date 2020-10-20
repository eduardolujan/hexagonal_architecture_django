# -*- coding: utf-8 -*-


from dataclasses import dataclass

from src.shared.domain.entities import Entity
from src.users.domain.value_objects import (UserId, Username, UserPassword, UserEmail)


@dataclass(frozen=True)
class User(Entity):
    id: UserId
    username: Username
    password: UserPassword
    email: UserEmail
