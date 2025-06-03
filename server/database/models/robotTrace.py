from typing import List
from ..interfaces.base import BaseRepository
from ..interfaces.robotTrace import RobotTrace, RobotTraceId, IRobotTraceRepository
from ..database import Database


class RobotTraceRepository(BaseRepository, IRobotTraceRepository):
    """RobotTrace Repo."""
    
    def __init__(self):
        # To be Implemented 
        super().__init__()
        self.cursor = Database().getCursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS robot_trace "
            "(id TEXT PRIMARY KEY, " \
            "robotid TEXT, " \
            "vitesse_instant REAL, " \
            "ds_ultrasons REAL, " \
            "status_deplacement TEXT, " \
            "orientation REAL, " \
            "status_pince INTEGER, " \
            "timestamp TEXT)")

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