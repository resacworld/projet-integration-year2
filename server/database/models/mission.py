"""
Ce fichier a été complété par un assistant IA, (il a fait toutes les tâches répétitives des fichiers dans le dossier parent "models").
"""

import uuid
from typing import List, Optional
from ..interfaces.base import BaseRepository
from ..interfaces.mission import Mission, MissionId, IMissionRepository
from ..database import Database

class MissionRepository(BaseRepository, IMissionRepository):
    """
    Mission Repository implementing CRUD operations.
    """

    def __init__(self):
        super().__init__()
        self.conn = Database.getConnection()
        self.cursor = self.conn.cursor()

        # Create the mission table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mission (
                id TEXT PRIMARY KEY,
                name TEXT,
                description TEXT
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

        self.cursor.execute("SELECT * FROM mission")
        rows = self.cursor.fetchall()
        return [Mission(
            id=MissionId(id=row[0]),
            name=row[1],
            description=row[2]
        ) for row in rows]

    def find_by_id(self, id: str) -> Optional[Mission]:
        """
        Find a mission by its ID.
        """

        self.cursor.execute(f"SELECT * FROM mission WHERE id = \"{id}\"")
        row = self.cursor.fetchone()
        return Mission(
            id=MissionId(id=row[0]),
            name=row[1],
            description=row[2]
        ) if row else None

    def add(self, mission: Mission) -> None:
        """
        Add a new mission to the database.
        """

        self.cursor.execute(f"""
            INSERT INTO mission (id, name, description)
            VALUES (
                \"{self.next_identity()}\", 
                \"{mission.name}\", 
                \"{mission.description}\""
            )
        """)
        self.conn.commit()

    def update(self, mission: Mission) -> None:
        """
        Update an existing mission in the database.
        """

        raise NotImplementedError("Method is not implemented yet.")

    def delete(self, id: str) -> None:
        """
        Delete a mission by its ID.
        """

        raise NotImplementedError("Method should not be implemented (due of the laws, for tracability).")
        # self.cursor.execute("DELETE FROM mission WHERE id = \"{id}\"")
        # self.conn.commit()