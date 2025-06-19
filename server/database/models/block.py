"""
This file was partially completed by an AI assistant, which handled all the repetitive tasks for files in the parent "models" directory.
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

    def __init__(self):
        """
        Intialisation of the repository
        """
        
        super().__init__()
        self.conn = Database.getConnection()
        self.cursor = self.conn.cursor()

        # Create the blocks table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS blocks (
                id TEXT PRIMARY KEY,
                mission_id TEXT,
                block_nb INTEGER,
                block_order INTEGER,
                FOREIGN KEY (mission_id) REFERENCES missions (id)
            )
        """)
        self.conn.commit()

    def next_identity(self) -> BlockId:
        """!
        Generate a new unique identifier for a Block record.
        @return A new BlockId object with a unique ID.
        """

        return BlockId(id=str(uuid.uuid4()))

    def find_all(self) -> List[Block]:
        """!
        Retrieve all Blocks from the database.
        @return List of Block objects.
        """

        self.cursor.execute("SELECT * FROM blocks")
        rows = self.cursor.fetchall()
        return [Block(
            id=BlockId(id=row[0]),
            mission_id=MissionId(id=row[1]),
            block_nb=row[2],
            block_order=row[3]
        ) for row in rows]

    def find_by_id(self, id: str | BlockId) -> Optional[Block]:
        """!
        Find a Block by its ID.
        @param id: The ID of the Block to find, can be a string or BlockId.
        @return Block if found, otherwise None.
        """

        self.cursor.execute(f"SELECT * FROM blocks WHERE id = \"{id}\"")
        row = self.cursor.fetchone()
        return None if row == None else Block(
            id=BlockId(id=row[0]),
            mission_id=MissionId(id=row[1]),
            block_nb=row[2],
            block_order=row[3]
        ) if row else None
    
    def find_many_by_mission_id(self, mission_id: str | MissionId) -> List[Block]:
        """!
        Find all Blocks associated with a specific Mission ID.
        @param mission_id: The ID of the Mission to find Blocks for, can be a string or MissionId.
        @return List of Block associated with the specified Mission ID.
        """

        self.cursor.execute(f"SELECT * FROM blocks WHERE mission_id = \"{mission_id}\" ORDER BY block_order ASC")
        rows = self.cursor.fetchall()
        return [Block(
            id=BlockId(id=row[0]),
            mission_id=MissionId(id=row[1]),
            block_nb=row[2],
            block_order=row[3]
        ) for row in rows]


    def add(self, block: Block) -> None:
        """!
        Add a new Block to the database.
        @param block: The Block to add.
        @note: If the block ID is not defined, a new unique ID will be generated.
        """

        self.cursor.execute(f"""
            INSERT INTO blocks (id, mission_id, block_nb, block_order)
            VALUES (
                \"{block.id if block.id != None else self.next_identity()}\", 
                \"{block.mission_id}\",
                {block.block_nb},
                {block.block_order}
            )
        """)
        self.conn.commit()

    def update(self, block: Block) -> None:
        """!
        Update an existing Block in the database.
        @param block: The Block with updated information.
        @raises NotImplementedError: This method is not implemented yet.
        """

        raise NotImplementedError("Method is not implemented yet.")

    def delete(self, id: str | BlockId) -> None:
        """!
        Delete a Block by its ID.
        @param id: The ID of the Block to delete, can be a string or BlockId.
        @raises NotImplementedError: This method is not implemented due to standards for traceability.
        """

        raise NotImplementedError("Method should not be implemented (due to standards, for traceability).")
        # self.cursor.execute("DELETE FROM blocks WHERE id = \"{id}\"")
        # self.conn.commit()