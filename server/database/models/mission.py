"""
Ce fichier a été complété par un assistant IA, (il a fait toutes les tâches répétitives des fichiers dans le dossier parent "models").
"""

import uuid
from typing import List, Optional
from ..interfaces.base import BaseRepository
from ..interfaces.mission import Mission, MissionId, IMissionRepository
from ..interfaces.robot import RobotId
from ..database import Database

class MissionRepository(BaseRepository, IMissionRepository):
    """
    Mission Repository implementing CRUD operations.
    """

    # _instance = None

    # def __new__(cls, *args, **kwargs):
    #     """
    #     Singleton pattern to ensure only one instance of BlockRepository exists.
    #     """
    #     if not cls._instance:
    #         cls._instance = super().__new__(cls, *args, **kwargs)
    #     return cls._instance

    def __init__(self):
        super().__init__()
        self.conn = Database.getConnection()
        self.cursor = self.conn.cursor()

        # Create the missions table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS missions (
                id TEXT PRIMARY KEY,
                robot_id TEXT,
                name TEXT,
                finished INTEGER DEFAULT 0,
                executing INTEGER DEFAULT 0,
                FOREIGN KEY (robot_id) REFERENCES robots (id)
            )
        """)
        self.conn.commit()

    def next_identity(self) -> MissionId:
        """
        Generate a new unique identifier for a Mission record.
        """

        return MissionId(id=str(uuid.uuid4()))

    def find_all(self) -> List[Mission]:
        """
        Retrieve all missions from the database.
        """

        self.cursor.execute("SELECT * FROM missions")
        rows = self.cursor.fetchall()
        return [Mission(
            id=MissionId(id=row[0]),
            robot_id=RobotId(id=row[1]),
            name=row[2],
            finished=bool(row[3]),
            executing=bool(row[4])
        ) for row in rows]

    def find_by_id(self, id: str | MissionId) -> Optional[Mission]:
        """
        Find a mission by its ID.
        """

        self.cursor.execute(f"SELECT * FROM missions WHERE id = \"{id}\"")
        row = self.cursor.fetchone()
        return None if row == None else Mission(
            id=MissionId(id=row[0]),
            robot_id=RobotId(id=row[1]),
            name=row[2],
            finished=bool(row[3]),
            executing=bool(row[4])
        ) if row else None
    
    def find_all_by_robot_id(self, robot_id: str | RobotId) -> Optional[List[Mission]]:
        self.cursor.execute(f"SELECT * FROM missions WHERE robot_id =  \"{robot_id}\"")
        rows = self.cursor.fetchall()
        return [Mission(
            id=MissionId(id=row[0]),
            robot_id=RobotId(id=row[1]),
            name=row[2],
            finished=bool(row[3]),
            executing=bool(row[4])
        ) for row in rows]
    
    def find_next_mission_by_robot_id(self, robot_id: str | RobotId) -> Optional[Mission]:
        """
        Find the next mission for a given robot by its ID.
        """

        self.cursor.execute(f"SELECT * FROM missions WHERE robot_id = \"{robot_id}\" AND finished = 0 AND executing = 0 LIMIT 1")
        row = self.cursor.fetchone()
        return None if row == None else Mission(
            id=MissionId(id=row[0]),
            robot_id=RobotId(id=row[1]),
            name=row[2],
            finished=bool(row[3]),
            executing=bool(row[4])
        ) if row else None
    

    def find_by_robot_id_and_executing(self, robot_id: str | RobotId, executing: bool) -> Mission:
        """
        Find all missions for a given robot ID that are currently executing.
        """

        self.cursor.execute(f"""
            SELECT * FROM missions 
            WHERE robot_id = \"{robot_id}\" AND executing = {executing} LIMIT 1
        """)
        row = self.cursor.fetchone()
        return None if row == None else Mission(
            id=MissionId(id=row[0]),
            robot_id=RobotId(id=row[1]),
            name=row[2],
            finished=bool(row[3]),
            executing=bool(row[4])
        )

    def add(self, mission: Mission) -> None:
        """
        Add a new mission to the database.
        """

        self.cursor.execute(f"""
            INSERT INTO missions (id, robot_id, name, finished, executing)
            VALUES (
                \"{mission.id if mission.id != None else self.next_identity()}\", 
                \"{mission.robot_id}\",
                \"{mission.name}",
                {mission.finished},
                {mission.executing}
            )
        """)
        self.conn.commit()

    def update(self, mission: Mission) -> None:
        """
        Update an existing mission in the database.
        """

        self.cursor.execute(f"""
            UPDATE missions
            SET robot_id = \"{mission.robot_id}\",
                name = \"{mission.name}\",
                finished = {int(mission.finished)},
                executing = {int(mission.executing)}
            WHERE id = \"{mission.id}\"
        """)
        self.conn.commit()

    def update_execution_status(self, mission_id: str | MissionId, executing: bool, finished:bool=False) -> None:
        """
        Update an existing mission in the database.
        """

        self.cursor.execute(f"""
            UPDATE missions
            SET finished = {int(finished)},
                executing = {int(executing)}
            WHERE id = \"{str(mission_id)}\"
        """)
        self.conn.commit()

    def delete(self, id: str | MissionId) -> None:
        """
        Delete a mission by its ID.
        """

        raise NotImplementedError("Method should not be implemented (due of the laws, for tracability).")
        # self.cursor.execute("DELETE FROM missions WHERE id = \"{id}\"")
        # self.conn.commit()