from src.shared.domain.value_objects import Uuid, String, Email


class AppUserId(Uuid):
    pass

class Username(String):
    pass

class UserPassword(String):
    pass

class UserEmail(String):
    pass
