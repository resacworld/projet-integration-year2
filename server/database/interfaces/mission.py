from typing import List
from abc import ABC, abstractmethod
from .base import BaseIdentifier, BaseObject
from .robot import RobotId
import json

class MissionId(BaseIdentifier):
    """Value object holding Robot identity."""
    pass


class Mission(BaseObject):
    """Aggregate root, entity holding robot."""
    id: MissionId
    robot_id: RobotId
    name: str
    finished: bool
    executing: bool
    start_date: str
    end_date: str


class IMissionRepository(ABC):
    """Interface for handling robots persistence."""
    @abstractmethod
    def next_identity(self) -> MissionId:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def find_all(self) -> List[Mission]:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def find_by_id(self, id: MissionId) -> Mission:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def add(self, room: Mission) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def update(self, room: Mission) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def delete(self, id: MissionId) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")