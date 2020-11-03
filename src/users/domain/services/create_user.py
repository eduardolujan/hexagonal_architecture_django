# -*- coding: utf-8 -*-


from src.shared.domain.passwords import PasswordGenerator
from src.users.domain.entities import User
from src.users.domain.value_objects import UserId, Username, UserPassword, UserEmail


class CreateUser:
    """
    Name constructors to create User
    """
    @staticmethod
    def create_base_user(_id: str,
                         username: str,
                         password: str,
                         email: str,
                         password_generator: PasswordGenerator = None):
        """
        Create User
        @param _id:
        @type _id:
        @param username:
        @type username:
        @param password:
        @type password:
        @param email:
        @type email:
        @param password_generator:
        @type password_generator:
        @return:
        @rtype:
        """

        if not password_generator:
            raise ValueError("Not assigned password_generator")

        app_user_id = UserId(id)
        username = Username(username)
        encrypted_password = password_generator.create(password)
        password = UserPassword(encrypted_password)
        email = UserEmail(email)

        app_user = User(
            id=app_user_id,
            username=username,
            password=password,
            email=email
        )
        return app_user



