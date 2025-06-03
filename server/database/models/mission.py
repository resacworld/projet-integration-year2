from typing import List
from ..interfaces.base import BaseRepository
from ..interfaces.mission import Mission, MissionId, IMissionRepository
from ..database import Database


class MissionRepository(BaseRepository, IMissionRepository):
    """Mission Repository."""

    def __init__(self):
        # To be Implemented 
        super().__init__()
        self.cursor = Database.getCursor()

    def next_identity(self) -> MissionId:
        # To be Implemented 
        raise NotImplementedError

    def find_all(self) -> List[Mission]:
        # To be Implemented 
        raise NotImplementedError

    def find_by_id(self, id: MissionId) -> Mission:
        # To be Implemented 
        raise NotImplementedError

    def add(self, room: Mission) -> None:
        # To be Implemented 
        raise NotImplementedError

    def update(self, room: Mission) -> None:
        # To be Implemented 
        raise NotImplementedError

    def delete(self, id: MissionId) -> None:
        # To be Implemented 
        raise NotImplementedError