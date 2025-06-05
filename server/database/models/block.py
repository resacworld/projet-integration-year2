"""
Ce fichier a été complété par un assistant IA, (il a fait toutes les tâches répétitives des fichiers dans le dossier parent "models").
"""

import uuid
from typing import List, Optional
from ..interfaces.base import BaseRepository
from ..interfaces.block import Block, BlockId, IBlockRepository
from ..interfaces.mission import MissionId
from ..database import Database

class BlockRepository(BaseRepository, IBlockRepository):
    """
    Block Repository implementing CRUD operations.
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

        # Create the blocks table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS blocks (
                id TEXT PRIMARY KEY,
                mission_id TEXT,
                block_nb INTEGER,
                status_pince BOOLEAN,
                FOREIGN KEY (mission_id) REFERENCES missions (id)
            )
        """)
        self.conn.commit()

    def next_identity(self) -> BlockId:
        """
        Generate a new unique identifier for a Block record.
        """

        return BlockId(id=str(uuid.uuid4()))

    def find_all(self) -> List[Block]:
        """
        Retrieve all Blocks from the database.
        """

        self.cursor.execute("SELECT * FROM blocks")
        rows = self.cursor.fetchall()
        return [Block(
            id=BlockId(id=row[0]),
            mission_id=MissionId(id=row[1]),
            block_nb=row[2],
            status_pince=row[3]
        ) for row in rows]

    def find_by_id(self, id: str | BlockId) -> Optional[Block]:
        """
        Find a Block by its ID.
        """

        self.cursor.execute(f"SELECT * FROM blocks WHERE id = \"{id}\"")
        row = self.cursor.fetchone()
        return None if row == None else Block(
            id=BlockId(id=row[0]),
            mission_id=MissionId(id=row[1]),
            block_nb=row[2],
            status_pince=row[3]
        ) if row else None
    
    def find_by_mission_id(self, mission_id: str | MissionId) -> List[Block]:
        """
        Find all Blocks associated with a specific Mission ID.
        """

        self.cursor.execute(f"SELECT * FROM blocks WHERE mission_id = \"{mission_id}\"")
        rows = self.cursor.fetchall()
        return [Block(
            id=BlockId(id=row[0]),
            mission_id=MissionId(id=row[1]),
            block_nb=row[2],
            status_pince=row[3]
        ) for row in rows]


    def add(self, block: Block) -> None:
        """
        Add a new Block to the database.
        """

        self.cursor.execute(f"""
            INSERT INTO blocks (id, mission_id, block_nb, status_pince)
            VALUES (
                \"{block.id if block.id != None else self.next_identity()}\", 
                \"{block.mission_id}\",
                {block.block_nb},
                {int(block.status_pince)}
            )
        """)
        self.conn.commit()

    def update(self, block: Block) -> None:
        """
        Update an existing Block in the database.
        """

        raise NotImplementedError("Method is not implemented yet.")

    def delete(self, id: str | BlockId) -> None:
        """
        Delete a Block by its ID.
        """

        raise NotImplementedError("Method should not be implemented (due of the laws, for tracability).")
        # self.cursor.execute("DELETE FROM blocks WHERE id = \"{id}\"")
        # self.conn.commit()