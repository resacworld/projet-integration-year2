"""
This module contains basic classes from which all domain objects will inherit.
"""
from pydantic import BaseModel, ConfigDict
import uuid


class BaseIdentifier(BaseModel):
    """Value object holding Component identity."""
    id: str

    def __str__(self):
        return self.id
    
class BaseObject(BaseModel):
    """Base class for all domain objects."""
    id: BaseIdentifier

    def to_json(self):
        """Convert the object to a JSON serializable dictionary."""
        return {str(k): (v.id if isinstance(v, BaseIdentifier) else v) for k, v in self.__dict__.items()}


class BaseRepository:
    """Base repository with common functionality."""
    def next_identity(self):
        return str(uuid.uuid4())