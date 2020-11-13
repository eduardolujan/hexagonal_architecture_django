# -*- coding: utf-8 -*-


from dataclasses import dataclass

from modules.shared.domain.entities import Entity
from modules.users.domain.value_objects import (UserId, Username, Password, Email)


@dataclass(frozen=True)
class AppUser(Entity):
    id: UserId
    username: Username
    password: Password
    email: Email


app_user_id = UserId('f0aa2fd1-8d1a-4042-869e-03e03f9e2012')
username = Username('root')
password = Password('password')
email = Email('eduardo.lujan.p@gmail.com')
app_user = AppUser(
    id=app_user_id,
    username=username,
    password=password,
    email=email
)
var = app_user.as_dict()
pass
