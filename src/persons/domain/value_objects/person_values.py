# -*- utf-8  -*-


from src.shared.domain.value_objects import String, Uuid


class PersonId(Uuid):
    """
    Person ID as UUID
    """
    pass


class Name(String):
    """
    Person Name as String
    """
    pass


class LastName(String):
    """
    Person Last Name
    """
    pass


class SecondLastName(String):
    """
    Person Second Last Name
    """
    pass
