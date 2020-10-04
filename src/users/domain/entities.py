

from dataclasses import dataclass

from src.shared.domain.entities import Entity
from src.shared.domain.value_objects import Uuid, String, Email


class AppUserId(Uuid):
    pass


class Username(String):
    pass

class UserPassword(String):
    pass

class UserEmail(String):
    pass


@dataclass(frozen=True)
class AppUser(Entity):
    id: AppUserId
    username: Username
    password: UserPassword
    email: UserEmail


app_user_id = AppUserId('f0aa2fd1-8d1a-4042-869e-03e03f9e2012')
username = Username('root')
password = String('password')
email = String('eduardo.lujan.p@gmail.com')
app_user = AppUser(
    id=app_user_id,
    username=username,
    password=password,
    email=email
)
var = app_user.as_dict()
