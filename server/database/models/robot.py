from typing import List
from ..interfaces.base import BaseRepository
from ..interfaces.robot import Robot, RobotId, IRobotRepository
from ..database import Database


class RobotRepository(BaseRepository, IRobotRepository):
    """Robot repository"""

    def __init__(self):
        # To be Implemented 
        super().__init__()

        self.cursor = Database().getCursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS robot "
            "(id TEXT PRIMARY KEY, " \
            "mac TEXT, " \
            "name TEXT, " \
            "description TEXT)")

    def next_identity(self) -> RobotId:
        # To be Implemented 
        raise NotImplementedError

    def find_all(self) -> List[Robot]:
        # To be Implemented 
        raise NotImplementedError

    def find_by_id(self, id: RobotId) -> Robot:
        # To be Implemented 
        raise NotImplementedError

    def add(self, room: Robot) -> None:
        # To be Implemented 
        raise NotImplementedError

    def update(self, room: Robot) -> None:
        # To be Implemented 
        raise NotImplementedError

    def delete(self, id: RobotId) -> None:
        # To be Implemented 
        raise NotImplementedError