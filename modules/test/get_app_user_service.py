from modules.users.domain.entities.user import (
    User as AppUserEntity,
    UserId as AppUserIdEntity
)


class GetAppUserService:
    def __init__(self, user_id_entity: AppUserIdEntity, app_user_repository: AbstractRepository):
        self.user_id_entity = user_id_entity
        self.app_user_repository = app_user_repository

    def __call__(self):
        return self.app_user_repository.get(self.user_id_entity)


if __name__ == '__main__':
    import django
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    django.setup()
    from modules.users.infrastructure.repository import AppUserRepository
    from had.app.models import Person
    pass

    repository = AppUserRepository()
    app_user_id = AppUserIdEntity('f0aa2fd1-8d1a-4042-869e-03e03f9e2012')
    app_user = AppUserEntity(id=app_user_id, username='root', password='password', email='eduardo.lujan.p@gmail.com')
    get_app_user = GetAppUserService(app_user_id, repository)
    var = get_app_user()
    pass
