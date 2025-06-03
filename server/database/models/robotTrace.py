from typing import List
from ..interfaces.base import BaseRepository
from ..interfaces.robotTrace import RobotTrace, RobotTraceId, IRobotTraceRepository


class RobotTraceRepository(BaseRepository, IRobotTraceRepository):
    """RobotTrace Repo."""
    
    def __init__(self):
        # To be Implemented 
        super().__init__()

    def next_identity(self) -> RobotTraceId:
        # To be Implemented 
        raise NotImplementedError

    def find_all(self) -> List[RobotTrace]:
        # To be Implemented 
        raise NotImplementedError

    def find_by_id(self, id: RobotTraceId) -> RobotTrace:
        # To be Implemented 
        raise NotImplementedError

    def add(self, room: RobotTrace) -> None:
        # To be Implemented 
        raise NotImplementedError

    def update(self, room: RobotTrace) -> None:
        # To be Implemented 
        raise NotImplementedError

    def delete(self, id: RobotTraceId) -> None:
        # To be Implemented 
        raise NotImplementedError