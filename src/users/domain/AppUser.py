import dataclasses

from src.shared.domain.entity import EntityID


class AppUserId(EntityID):
    def __init__(self, id):
        super().__init__(id)


@dataclasses.dataclass(frozen=True)
class AppUser:
    id: AppUserId
    username: str
    password: str
    email: str


app_user_id = AppUserId('f0aa2fd1-8d1a-4042-869e-03e03f9e2012')
app_user = AppUser(id=app_user_id, username='root', password='password', email='eduardo.lujan.p@gmail.com')
app_user = dataclasses.asdict(app_user)

pass
