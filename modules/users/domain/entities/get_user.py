# -*- coding: utf-8 -*-


from dataclasses import dataclass

from modules.shared.domain.entities import Entity
from modules.users.domain.value_objects import UserId


@dataclass(frozen=True)
class GetUser(Entity):
    id: UserId
