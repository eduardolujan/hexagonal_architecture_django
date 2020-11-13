# -*- coding: utf-8 -*-


from modules.shared.domain.passwords import PasswordGenerator
from modules.users.domain.entities import User
from modules.users.domain.value_objects import UserId, Username, Password, Email


class CreateUserService:
    """
    Create user entities
    """

    @staticmethod
    def create_user_entity(id: UserId = None,
                           username: Username = None,
                           password: Password = None,
                           email: Email = None):

        if not isinstance(id, UserId):
            raise ValueError(f"Parameter id: {id} "
                             f"is not instance of UserId")

        if not isinstance(username, Username):
            raise ValueError(f"Parameter username {username} "
                             f"is not instance of Username")

        if not isinstance(password, Password):
            raise ValueError(f"Parameter password {password} "
                             f"is not instance of Password")

        if not isinstance(email, Email):
            raise ValueError(f"Parameter email: {email} "
                             f"is not instance of Email")

        app_user = User(
            id=id,
            username=username,
            password=password,
            email=email
        )
        return app_user



