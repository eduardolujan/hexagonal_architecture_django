

from dataclasses import dataclass

from src.shared.domain.entities import Entity
from src.shared.domain.value_objects import Uuid


class AppUserId(Uuid):
    pass


@dataclass(frozen=True)
class AppUser(Entity):
    id: AppUserId
    username: str
    password: str
    email: str


app_user_id = AppUserId('f0aa2fd1-8d1a-4042-869e-03e03f9e2012')
app_user = AppUser(id=app_user_id, username='root', password='password', email='eduardo.lujan.p@gmail.com')
var = app_user.as_dict()


pass
