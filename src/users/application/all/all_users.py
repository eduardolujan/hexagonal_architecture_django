# -*- coding: utf-8 -*-


from src.users.domain.repository import UserRepository


class AllUsers:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def all(self):
        users = self.user_repository.all()
        return users
