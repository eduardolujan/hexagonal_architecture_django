
# -*- coding: utf-8 -*-


from modules.users.domain.entities import User as UserEntity
from modules.users.domain.domain_events import CreateUserDomainEvent
from modules.users.domain import value_objects


class CreateUserService:
    """
    Create user entities
    """

    @staticmethod
    def create_user_entity(id: value_objects.UserId = None,
                           username: value_objects.Username = None,
                           password: value_objects.Password = None,
                           email: value_objects.Email = None):

        if not isinstance(id, value_objects.UserId):
            raise ValueError(f"Parameter id: {id} "
                             f"is not instance of UserId")

        if not isinstance(username, value_objects.Username):
            raise ValueError(f"Parameter username {username} "
                             f"is not instance of Username")

        if not isinstance(password, value_objects.Password):
            raise ValueError(f"Parameter password {password} "
                             f"is not instance of Password")

        if not isinstance(email, value_objects.Email):
            raise ValueError(f"Parameter email: {email} "
                             f"is not instance of Email")

        user_entity = UserEntity(
            id=id,
            username=username,
            password=password,
            email=email
        )

        create_user_domain_event = CreateUserDomainEvent(
            id=id.value,
            username=username.value,
            password=password.value,
            email=email.value)

        user_entity.record(create_user_domain_event)

        return user_entity



