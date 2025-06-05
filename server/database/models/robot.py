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

        # Create the robots table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS robots (
                id TEXT PRIMARY KEY,
                mac TEXT,
                name TEXT
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

        self.cursor.execute("SELECT * FROM robots")
        rows = self.cursor.fetchall()
        return [Robot(
            id=RobotId(id=row[0]),
            mac=row[1],
            name=row[2]
        ) for row in rows]

    def find_by_id(self, id: str | RobotId) -> Optional[Robot]:
        """
        Find a robot by its ID.
        """

        self.cursor.execute(f"SELECT * FROM robots WHERE id = \"{id}\"")
        row = self.cursor.fetchone()
        return None if row == None else Robot(
            id=RobotId(id=row[0]),
            mac=row[1],
            name=row[2]
        ) if row else None

    def add(self, robot: Robot) -> None:
        """
        Add a new robot to the database.
        """

        self.cursor.execute(f"""
            INSERT INTO robots (id, mac, name)
            VALUES (
                \"{robot.id if robot.id != None else self.next_identity()}\", 
                \"{robot.mac}\", 
                \"{robot.name}\"
            )
        """)
        self.conn.commit()

    def update(self, robot: Robot) -> None:
        """
        Update an existing robot in the database.
        """

        raise NotImplementedError("Method is not implemented yet.")

    def delete(self, id: str | RobotId) -> None:
        """
        Delete a robot by its ID.
        """

        raise NotImplementedError("Method should not be implemented (due of the laws, for tracability).")
        # self.cursor.execute("DELETE FROM robots WHERE id = \"{id}\"")
        # self.conn.commit()