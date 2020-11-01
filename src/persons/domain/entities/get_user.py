# -*- coding: utf-8 -*-


from dataclasses import dataclass

from src.shared.domain.entities import Entity
from src.users.domain.value_objects import UserId


@dataclass(frozen=True)
class GetUser(Entity):
    id: UserId
