"""
Ce fichier a été complété par un assistant IA, (il a fait toutes les tâches répétitives des fichiers dans le dossier parent "models").
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
        super().__init__()
        self.conn = Database.getConnection()
        self.cursor = self.conn.cursor()

        # Create the robot table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS robot (
                id TEXT PRIMARY KEY,
                mac TEXT,
                name TEXT,
                description TEXT
            )
        """)
        self.conn.commit()

    def next_identity(self) -> RobotId:
        """
        Generate a new unique identifier for a Robot record.
        """
        
        return RobotId(id=str(uuid.uuid4()))

    def find_all(self) -> List[Robot]:
        """
        Retrieve all robots from the database.
        """

        self.cursor.execute("SELECT * FROM robot")
        rows = self.cursor.fetchall()
        return [Robot(
            id=RobotId(id=row[0]),
            mac=row[1],
            name=row[2],
            description=row[3]
        ) for row in rows]

    def find_by_id(self, id: str) -> Optional[Robot]:
        """
        Find a robot by its ID.
        """

        self.cursor.execute(f"SELECT * FROM robot WHERE id = \"{id}\"")
        row = self.cursor.fetchone()
        return Robot(
            id=RobotId(id=row[0]),
            mac=row[1],
            name=row[2],
            description=row[3]
        ) if row else None

    def add(self, robot: Robot) -> None:
        """
        Add a new robot to the database.
        """

        self.cursor.execute(f"""
            INSERT INTO robot (id, mac, name, description)
            VALUES (
                \"{self.next_identity()}\", 
                \"{robot.mac}\", 
                \"{robot.name}\", 
                \"{robot.description}\""
            )
        """)
        self.conn.commit()

    def update(self, robot: Robot) -> None:
        """
        Update an existing robot in the database.
        """

        raise NotImplementedError("Method is not implemented yet.")

    def delete(self, id: str) -> None:
        """
        Delete a robot by its ID.
        """

        raise NotImplementedError("Method should not be implemented (due of the laws, for tracability).")
        # self.cursor.execute("DELETE FROM robot WHERE id = \"{id}\"")
        # self.conn.commit()