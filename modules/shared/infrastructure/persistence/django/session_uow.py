# -*- coding: utf-8 -*-


from modules.shared.domain.repository.session_unit_of_work import SessionUnitOfWork


class SessionUnitOfWork(SessionUnitOfWork):
    """
    SessionUnitOfWork
    """
    def __init__(self, unit_of_work):
        self._unit_of_work = unit_of_work

    def add(self, entity) -> None:
        """
        Add the entity in the UOF to create
        @param entity: Entity instance
        @type entity: Entity
        """
        self._unit_of_work.add(entity)

    def update(self, entity) -> None:
        """
        Add the entity in the UOF to update
        @param entity: Entity instance
        @type entity: Entity
        """
        self._unit_of_work.add(entity)

