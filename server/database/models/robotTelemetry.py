"""
This file was partially completed by an AI assistant, which handled all the repetitive tasks for files in the parent "models" directory.
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

    def __init__(self):
        """!
        Intialisation of the repository
        """
        
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
        """!
        Generate a new unique identifier for a RobotTelemetry record.
        @return A new RobotTelemetryId object with a unique ID.
        """

        return RobotTelemetryId(id=str(uuid.uuid4()))

    def find_all(self) -> List[RobotTelemetry]:
        """!
        Retrieve all robot telemetry records from the database.
        @return List of RobotTelemetry objects.
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
        """!
        Find a robot telemetry record by its ID.
        @param id: The ID of the robot telemetry record to find.
        @return The RobotTelemetry object if found, otherwise None.
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
    
    def find_last_by_mission_id(self, mission_id: str | MissionId) -> RobotTelemetry:
        """!
        Find the last robot telemetry recorded, by the mission id.
        @param mission_id: The ID of the mission to find the last telemetry for.
        @return The last RobotTelemetry object for the given mission ID, or None if not found.
        """

        self.cursor.execute(f"SELECT * FROM robot_telemetries WHERE mission_id = \"{mission_id}\" ORDER BY timestamp DESC")
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
        """!
        Add a new robot telemetry record to the database.
        @param telemetry: The RobotTelemetry object to add.
        @return None
        """

        self.cursor.execute(f"""
            INSERT INTO robot_telemetries (
                id, mission_id, vitesse_instant, ds_ultrasons, status_deplacement,
                ligne, status_pince, timestamp
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
        """!
        Update an existing robot telemetry record in the database.
        @param telemetry: The RobotTelemetry object containing updated data.
        @raises NotImplementedError: This method is not implemented yet.
        """

        raise NotImplementedError("Method is not implemented yet.")

    def delete(self, id: str | RobotTelemetryId) -> None:
        """!
        Delete a robot telemetry record by its ID.
        @param id: The ID of the robot telemetry record to delete.
        @raises NotImplementedError: This method is not implemented due to standards for tracability.
        """

        raise NotImplementedError("Method should not be implemented (due to standards, for traceability).")
        # self.cursor.execute(f"DELETE FROM robot_telemetries WHERE id = \"{id}\"")
        # self.conn.commit()