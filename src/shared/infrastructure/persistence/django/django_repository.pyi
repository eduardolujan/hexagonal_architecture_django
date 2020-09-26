

from typing import List

from src.shared.domain.entity import Entity
from src.shared.domain.repository import AbstractRepository


class DjangoRepository(AbstractRepository):

    def add(self, entity): ...

    def edit(self, entity): ...

    def delete(self, entity): ...

    def search(self, **fields) -> : ...
