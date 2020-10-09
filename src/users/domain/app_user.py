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


app_user_id = AppUserId('f0aa2fd1-8d1a-4042-869e-03e03f9e2012')
username = Username('root')
password = UserPassword('password')
email = UserEmail('eduardo.lujan.p@gmail.com')
app_user = AppUser(
    id=app_user_id,
    username=username,
    password=password,
    email=email
)
var = app_user.as_dict()
pass
