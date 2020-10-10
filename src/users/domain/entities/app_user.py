# -*- coding: utf-8 -*-


from dataclasses import dataclass

from src.shared.domain.entities import Entity
from src.users.domain.value_objects import (AppUserId, Username, UserPassword, UserEmail)


@dataclass(frozen=True)
class AppUser(Entity):
    id: AppUserId
    username: Username
    password: UserPassword
    email: UserEmail
