from abc import ABC, abstractmethod
from typing import Optional, List, Set
from src.shared.domain.entities import Entity


class AbstractRepository(ABC):
    def __setattr__(self, key, value): ...

    @abstractmethod
    def get(self, entity: Entity) -> Optional[Entity]: ...

    @abstractmethod
    def create(self, entity: Entity): ...

    @abstractmethod
    def update(self, entity: Entity): ...

    @abstractmethod
    def delete(self, entity: Entity): ...

    @abstractmethod
    def search(self, entity: Entity): ...

    @abstractmethod
    def all(self) -> List[Entity]: ...
