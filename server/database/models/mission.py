"""
This file was partially completed by an AI assistant, which handled all the repetitive tasks for files in the parent "models" directory.
"""

import uuid
from typing import List, Optional
from ..interfaces.base import BaseRepository
from ..interfaces.mission import Mission, MissionId, IMissionRepository
from ..interfaces.robot import RobotId
from ..database import Database
from datetime import datetime

class MissionRepository(BaseRepository, IMissionRepository):
    """
    Mission Repository implementing CRUD operations.
    """

    def __init__(self):
        """!
        Intialisation of the repository
        """

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
                start_date TEXT,
                end_date TEXT,
                FOREIGN KEY (robot_id) REFERENCES robots (id)
            )
        """)
        self.conn.commit()

    def next_identity(self) -> MissionId:
        """!
        Generate a new unique identifier for a Mission record.
        @return A new MissionId object with a unique ID.
        """

        return MissionId(id=str(uuid.uuid4()))

    def find_all(self) -> List[Mission]:
        """!
        Retrieve all missions from the database.
        @return List of Mission objects.
        """

        self.cursor.execute("SELECT * FROM missions")
        rows = self.cursor.fetchall()
        return [Mission(
            id=MissionId(id=row[0]),
            robot_id=RobotId(id=row[1]),
            name=row[2],
            finished=bool(row[3]),
            executing=bool(row[4]),
            start_date=str(row[5]),
            end_date=str(row[6])
        ) for row in rows]

    def find_by_id(self, id: str | MissionId) -> Optional[Mission]:
        """!
        Find a mission by its ID.
        @param id: The ID of the mission to find, can be a string or MissionId.
        @return Mission object if found, otherwise None.
        """

        self.cursor.execute(f"SELECT * FROM missions WHERE id = \"{id}\"")
        row = self.cursor.fetchone()
        return None if row == None else Mission(
            id=MissionId(id=row[0]),
            robot_id=RobotId(id=row[1]),
            name=row[2],
            finished=bool(row[3]),
            executing=bool(row[4]),
            start_date=str(row[5]),
            end_date=str(row[6])
        ) if row else None
    
    def find_all_by_robot_id(self, robot_id: str | RobotId) -> Optional[List[Mission]]:
        """!
        Find all mission of a robot
        @param robot_id: The ID of the robot to find missions for, can be a string or RobotId.
        @return List of Mission objects if found, otherwise None.
        """

        self.cursor.execute(f"SELECT * FROM missions WHERE robot_id =  \"{robot_id}\"")
        rows = self.cursor.fetchall()
        return [Mission(
            id=MissionId(id=row[0]),
            robot_id=RobotId(id=row[1]),
            name=row[2],
            finished=bool(row[3]),
            executing=bool(row[4]),
            start_date=str(row[5]),
            end_date=str(row[6])
        ) for row in rows]
    
    def find_next_mission_by_robot_id(self, robot_id: str | RobotId) -> Optional[Mission]:
        """!
        Find the next mission for a given robot by its ID.
        @param robot_id: The ID of the robot to find the next mission for, can be a string or RobotId.
        @return Mission object if found, otherwise None.
        """

        self.cursor.execute(f"SELECT * FROM missions WHERE robot_id = \"{robot_id}\" AND finished = 0 AND executing = 0 LIMIT 1")
        row = self.cursor.fetchone()
        return None if row == None else Mission(
            id=MissionId(id=row[0]),
            robot_id=RobotId(id=row[1]),
            name=row[2],
            finished=bool(row[3]),
            executing=bool(row[4]),
            start_date=str(row[5]),
            end_date=str(row[6])
        ) if row else None
    

    def find_by_robot_id_and_executing(self, robot_id: str | RobotId, executing: bool) -> Mission:
        """!
        Find all missions for a given robot ID that are currently executing.
        @param robot_id: The ID of the robot to find missions for, can be a string or RobotId.
        @param executing: Boolean indicating whether to find missions that are currently executing.
        @return Mission object if found, otherwise None.
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
            executing=bool(row[4]),
            start_date=str(row[5]),
            end_date=str(row[6])
        )

    def add(self, mission: Mission) -> None:
        """!
        Add a new mission to the database.
        @param mission: The Mission object to add.
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
        """!
        Update an existing mission in the database.
        @param mission: The Mission object with updated information.
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

    def start_mission(self, mission_id: str | MissionId) -> None:
        """!
        Start a mission
        @param mission_id: The ID of the mission to start, can be a string or MissionId.
        """

        self.cursor.execute(f"""
            UPDATE missions
            SET finished = {int(False)},
                executing = {int(True)},
                start_date = \"{datetime.now().isoformat()}\"
            WHERE id = \"{str(mission_id)}\"
        """)
        self.conn.commit()

    def end_mission(self, mission_id: str | MissionId) -> None:
        """!
        End current running mission
        @param mission_id: The ID of the mission to end, can be a string or MissionId.
        """
        
        self.cursor.execute(f"""
            UPDATE missions
            SET finished = {int(True)},
                executing = {int(False)},
                end_date = \"{datetime.now().isoformat()}\"
            WHERE id = \"{str(mission_id)}\"
        """)
        self.conn.commit()

    def delete(self, id: str | MissionId) -> None:
        """!
        Delete a mission by its ID.
        @param id: The ID of the mission to delete, can be a string or MissionId.
        """

        raise NotImplementedError("Method should not be implemented (due to standards, for traceability).")
        # self.cursor.execute("DELETE FROM missions WHERE id = \"{id}\"")
        # self.conn.commit()