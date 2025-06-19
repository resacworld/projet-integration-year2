"""
This file was partially completed by an AI assistant, which handled all the repetitive tasks for files in the parent "models" directory.
"""

import uuid
from typing import List, Optional
from ..interfaces.base import BaseRepository
from ..interfaces.robot import Robot, RobotId, IRobotRepository
from ..database import Database

class RobotRepository(BaseRepository, IRobotRepository):
    """
    Robot repository implementing CRUD operations.
    """

    def __init__(self):
        """!
        Intialisation of the repository
        """
        
        super().__init__()
        self.conn = Database.getConnection()
        self.cursor = self.conn.cursor()

        # Create the robots table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS robots (
                id TEXT PRIMARY KEY,
                name TEXT
            )
        """)
        self.conn.commit()

    def next_identity(self) -> RobotId:
        """!
        Generate a new unique identifier for a Robot record.
        @return A new RobotId object with a unique ID.
        """
        
        return RobotId(id=str(uuid.uuid4()))

    def find_all(self) -> List[Robot]:
        """!
        Retrieve all robots from the database.
        @return List of Robot objects.
        """

        self.cursor.execute("SELECT * FROM robots")
        rows = self.cursor.fetchall()
        return [Robot(
            id=RobotId(id=row[0]),
            name=row[1]
        ) for row in rows]

    def find_by_id(self, id: str | RobotId) -> Optional[Robot]:
        """!
        Find a robot by its ID.
        @param id: The ID of the robot to find, can be a string or RobotId.
        @return Robot object if found, otherwise None.
        """

        self.cursor.execute(f"SELECT * FROM robots WHERE id = \"{id}\"")
        row = self.cursor.fetchone()
        return None if row == None else Robot(
            id=RobotId(id=row[0]),
            name=row[1]
        ) if row else None

    def add(self, robot: Robot) -> None:
        """!
        Add a new robot to the database.
        @param robot: The Robot object to add.
        """

        self.cursor.execute(f"""
            INSERT INTO robots (id, name)
            VALUES (
                \"{robot.id if robot.id != None else self.next_identity()}\",
                \"{robot.name}\"
            )
        """)
        self.conn.commit()

    def update(self, robot: Robot) -> None:
        """!
        Update an existing robot in the database.
        @param robot: The Robot object with updated information.
        @raises NotImplementedError: This method is not implemented yet.
        """

        raise NotImplementedError("Method is not implemented yet.")

    def delete(self, id: str | RobotId) -> None:
        """!
        Delete a robot by its ID.
        @param id: The ID of the robot to delete, can be a string or RobotId.
        @raises NotImplementedError: This method is not implemented due to standards for traceability.
        """

        raise NotImplementedError("Method should not be implemented (due to standards, for traceability).")
        # self.cursor.execute("DELETE FROM robots WHERE id = \"{id}\"")
        # self.conn.commit()