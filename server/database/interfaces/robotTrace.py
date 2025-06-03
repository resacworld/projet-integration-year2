from typing import List
from abc import ABC, abstractmethod
from pydantic import BaseModel
from .base import BaseIdentifier


class RobotTraceId(BaseIdentifier):
    """Value object holding RobotTrace identity."""
    pass


class RobotTrace(BaseModel):
    """Aggregate root, entity holding robotTrace."""
    id: RobotTraceId
    name: str
    description: str


class IRobotTraceRepository(ABC):
    """Interface for handling robotTraces persistence."""
    @abstractmethod
    def next_identity(self) -> RobotTraceId:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[RobotTrace]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: RobotTraceId) -> RobotTrace:
        raise NotImplementedError

    @abstractmethod
    def add(self, room: RobotTrace) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, room: RobotTrace) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: RobotTraceId) -> None:
        raise NotImplementedError