from typing import List
from abc import ABC, abstractmethod
from pydantic import BaseModel
from .base import BaseIdentifier


class RobotId(BaseIdentifier):
    """Value object holding Robot identity."""
    pass


class Robot(BaseModel):
    """Aggregate root, entity holding robot."""
    id: RobotId
    mac: str
    name: str
    description: str


class IRobotRepository(ABC):
    """Interface for handling robots persistence."""
    @abstractmethod
    def next_identity(self) -> RobotId:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def find_all(self) -> List[Robot]:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def find_by_id(self, id: RobotId) -> Robot:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def add(self, room: Robot) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def update(self, room: Robot) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def delete(self, id: RobotId) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")