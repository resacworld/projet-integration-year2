"""
Ce fichier a été complété par un assistant IA, (il a fait toutes les tâches répétitives des fichiers dans le dossier parent "models").
"""

import uuid
from typing import List
from ..interfaces.base import BaseRepository
from ..interfaces.robotTelemetry import RobotTelemetry, RobotTelemetryId, IRobotTelemetryRepository
from ..interfaces.mission import MissionId
from ..database import Database


class RobotTelemetryRepository(BaseRepository, IRobotTelemetryRepository):
    """
    RobotTelemetry repository implementing CRUD operations.
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

        # Create the robot_telemetries table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS robot_telemetries (
                id TEXT PRIMARY KEY,
                mission_id TEXT,
                vitesse_instant REAL,
                ds_ultrasons REAL,
                status_deplacement TEXT,
                ligne INTEGER,
                status_pince INTEGER,
                timestamp TEXT,
                FOREIGN KEY (mission_id) REFERENCES missions (id)
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
        
        self.cursor.execute("SELECT * FROM robot_telemetries")
        rows: List[RobotTelemetry] = self.cursor.fetchall()

        print(rows[0])

        return [RobotTelemetry(
            id=RobotTelemetryId(id=row[0]),
            mission_id=MissionId(id=row[1]),
            vitesse_instant=row[2],
            ds_ultrasons=row[3],
            status_deplacement=row[4],
            ligne=row[5],
            status_pince=bool(row[6]),  # Convert integer to boolean
            timestamp=row[7]
        ) for row in rows]

    def find_by_id(self, id: str | RobotTelemetryId) -> RobotTelemetry:
        """
        Find a robot telemetry record by its ID.
        """

        self.cursor.execute(f"SELECT * FROM robot_telemetries WHERE id = \"{id}\"")
        row = self.cursor.fetchone()
        return None if row == None else RobotTelemetry(
            id=RobotTelemetryId(id=row[0]),
            mission_id=MissionId(id=row[1]),
            vitesse_instant=row[2],
            ds_ultrasons=row[3],
            status_deplacement=row[4],
            ligne=row[5],
            status_pince=bool(row[6]),  # Convert integer to boolean
            timestamp=row[7]
        )

    def add(self, telemetry: RobotTelemetry) -> None:
        """
        Add a new robot telemetry record to the database.
        """

        self.cursor.execute(f"""
            INSERT INTO robot_telemetries (
                id, mission_id, vitesse_instant, ds_ultrasons, status_deplacement,
                orientation, status_pince, timestamp
            ) VALUES (
                \"{telemetry.id if telemetry.id != None else self.next_identity()}\", 
                \"{telemetry.mission_id}\", 
                {telemetry.vitesse_instant}, 
                {telemetry.ds_ultrasons}, 
                \"{telemetry.status_deplacement}\", 
                {telemetry.ligne}, 
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

    def delete(self, id: str | RobotTelemetryId) -> None:
        """
        Delete a robot telemetry record by its ID.
        """

        raise NotImplementedError("Method should not be implemented (due of the laws, for tracability).")
        # self.cursor.execute(f"DELETE FROM robot_telemetries WHERE id = \"{id}\"")
        # self.conn.commit()