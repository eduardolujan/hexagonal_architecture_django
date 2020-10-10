
from uuid import UUID

from src.shared.domain.passwords import PasswordGenerator
from src.users.domain.entities import AppUser
from src.users.domain.value_objects import AppUserId, Username, UserPassword, UserEmail


class CreateUser:
    """
    Name constructors to create User
    """
    @staticmethod
    def create_base_user(id: str, username: str, password: str, email: str,
                         password_generator: PasswordGenerator = None):

        if not password_generator:
            raise ValueError("Not assigned password_generator")

        app_user_id = AppUserId(id)
        username = Username(username)
        encrypted_password = password_generator.make(password)
        password = UserPassword(encrypted_password)
        email = UserEmail(email)

        app_user = AppUser(
            id=app_user_id,
            username=username,
            password=password,
            email=email
        )
        return app_user



