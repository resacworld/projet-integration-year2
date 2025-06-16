from typing import List
from abc import ABC, abstractmethod
from .base import BaseIdentifier, BaseObject
from .mission import MissionId


class BlockId(BaseIdentifier):
    """Value object holding Block identity."""
    pass

class Block(BaseObject):
    """Aggregate root, entity holding Block."""
    id: BlockId
    mission_id: MissionId
    block_nb: int
    block_order: int


class IBlockRepository(ABC):
    """Interface for handling Block persistence."""
    @abstractmethod
    def next_identity(self) -> BlockId:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def find_all(self) -> List[Block]:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def find_by_id(self, id: BlockId) -> Block:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def add(self, room: Block) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def update(self, room: Block) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")

    @abstractmethod
    def delete(self, id: BlockId) -> None:
        raise NotImplementedError("Method is not implemented (abstract).")