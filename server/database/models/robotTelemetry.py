"""
Ce fichier a été complété par un assistant IA, (il a fait toutes les tâches répétitives des fichiers dans le dossier parent "models").
"""

import uuid
from typing import List
from ..interfaces.base import BaseRepository
from ..interfaces.robotTelemetry import RobotTelemetry, RobotTelemetryId, IRobotTelemetryRepository
from ..database import Database


class RobotTelemetryRepository(BaseRepository, IRobotTelemetryRepository):
    """
    RobotTelemetry repository implementing CRUD operations.
    """

    def __init__(self):
        super().__init__()
        self.conn = Database.getConnection()
        self.cursor = self.conn.cursor()

        # Create the robot telemetry table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS robot_telemetry (
                id TEXT PRIMARY KEY,
                robotid TEXT,
                vitesse_instant REAL,
                ds_ultrasons REAL,
                status_deplacement TEXT,
                orientation REAL,
                status_pince INTEGER,
                timestamp TEXT
            )
        """)
        self.conn.commit()

    def next_identity(self) -> RobotTelemetryId:
        """
        Generate a new unique identifier for a RobotTelemetry record.
        """

        return RobotTelemetryId(id=str(uuid.uuid4()))

    def find_all(self) -> List[RobotTelemetry]:
        """
        Retrieve all robot telemetry records from the database.
        """
        
        self.cursor.execute("SELECT * FROM robot_telemetry")
        rows: List[RobotTelemetry] = self.cursor.fetchall()

        print(rows[0])

        return [RobotTelemetry(
            id=RobotTelemetryId(id=row[0]),
            robotid=row[1],
            vitesse_instant=row[2],
            ds_ultrasons=row[3],
            status_deplacement=row[4],
            orientation=row[5],
            status_pince=bool(row[6]),  # Convert integer to boolean
            timestamp=row[7]
        ) for row in rows]

    def find_by_id(self, id: str) -> RobotTelemetry:
        """
        Find a robot telemetry record by its ID.
        """

        self.cursor.execute(f"SELECT * FROM robot_telemetry WHERE id = \"{id}\"")
        row = self.cursor.fetchone()
        if row:
            return RobotTelemetry(
                id=RobotTelemetryId(id=row[0]),
                robotid=row[1],
                vitesse_instant=row[2],
                ds_ultrasons=row[3],
                status_deplacement=row[4],
                orientation=row[5],
                status_pince=bool(row[6]),  # Convert integer to boolean
                timestamp=row[7]
            )
        return None

    def add(self, telemetry: RobotTelemetry) -> None:
        """
        Add a new robot telemetry record to the database.
        """

        self.cursor.execute(f"""
            INSERT INTO robot_telemetry (
                id, robotid, vitesse_instant, ds_ultrasons, status_deplacement,
                orientation, status_pince, timestamp
            ) VALUES (
                \"{self.next_identity()}\", 
                \"{telemetry.robotid}\", 
                {telemetry.vitesse_instant}, 
                {telemetry.ds_ultrasons}, 
                \"{telemetry.status_deplacement}\", 
                {telemetry.orientation}, 
                {telemetry.status_pince}, 
                \"{telemetry.timestamp}\"
            )
        """)
        self.conn.commit()

    def update(self, telemetry: RobotTelemetry) -> None:
        """
        Update an existing robot telemetry record in the database.
        """

        raise NotImplementedError("Method is not implemented yet.")

    def delete(self, id: str) -> None:
        """
        Delete a robot telemetry record by its ID.
        """

        raise NotImplementedError("Method should not be implemented (due of the laws, for tracability).")
        # self.cursor.execute(f"DELETE FROM robot_telemetry WHERE id = \"{id}\"")
        # self.conn.commit()