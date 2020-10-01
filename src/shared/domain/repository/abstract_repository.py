from abc import ABC, abstractmethod
from typing import Optional, List
from src.shared.domain.entities import Entity


class AbstractRepository(ABC):

    def __setattr__(self, key, value): ...

    @abstractmethod
    def get(self, entity: Entity) -> Optional[Entity]: ...

    @abstractmethod
    def create(self, entity: Entity) -> Optional[bool]: ...

    @abstractmethod
    def update(self, entity: Entity) -> Optional[bool]: ...

    @abstractmethod
    def delete(self, entity: Entity) -> Optional[bool]: ...

    @abstractmethod
    def search(self, entity: Entity) -> List[Entity]: ...

    @abstractmethod
    def all(self) -> List[Entity]: ...
