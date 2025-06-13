from typing import List
from abc import ABC, abstractmethod
from .base import BaseIdentifier, BaseObject


class RobotId(BaseIdentifier):
    """Value object holding Robot identity."""
    pass


class Robot(BaseObject):
    """Aggregate root, entity holding robot."""
    id: RobotId
    mac: str
    name: str


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