from typing import List
from abc import ABC, abstractmethod
from pydantic import BaseModel
from .base import BaseIdentifier, BaseObject
from .mission import MissionId


class RobotTelemetryId(BaseIdentifier):
    """Value object holding RobotTelemetry identity."""
    pass


class RobotTelemetry(BaseObject):
    """Aggregate root, entity holding robotTelemetry."""
    id: RobotTelemetryId
    mission_id: MissionId
    vitesse_instant: float
    ds_ultrasons: float
    status_deplacement: str
    orientation: float
    status_pince: bool
    timestamp: str


class IRobotTelemetryRepository(ABC):
    """Interface for handling RobotTelemetry persistence."""
    @abstractmethod
    def next_identity(self) -> RobotTelemetryId:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def find_all(self) -> List[RobotTelemetry]:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def find_by_id(self, id: RobotTelemetryId) -> RobotTelemetry:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def add(self, room: RobotTelemetry) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def update(self, room: RobotTelemetry) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def delete(self, id: RobotTelemetryId) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")