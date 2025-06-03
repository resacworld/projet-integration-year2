from typing import List
from abc import ABC, abstractmethod
from pydantic import BaseModel
from .base import BaseIdentifier


class MissionId(BaseIdentifier):
    """Value object holding Robot identity."""
    pass


class Mission(BaseModel):
    """Aggregate root, entity holding robot."""
    id: MissionId
    name: str
    description: str


class IMissionRepository(ABC):
    """Interface for handling robots persistence."""
    @abstractmethod
    def next_identity(self) -> MissionId:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[Mission]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: MissionId) -> Mission:
        raise NotImplementedError

    @abstractmethod
    def add(self, room: Mission) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, room: Mission) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: MissionId) -> None:
        raise NotImplementedError