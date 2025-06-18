"""
This module contains basic classes from which all domain objects will inherit.
This file was partially completed by an AI assistant, which handled all the repetitive tasks for files in the parent "models" directory.
"""

from pydantic import BaseModel
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
        """!
        Convert the object to a JSON serializable dictionary.
        @return Dictionary representation of the object.
        """
        return {str(k): (v.id if isinstance(v, BaseIdentifier) else v) for k, v in self.__dict__.items()}


class BaseRepository:
    def next_identity(self):
        """!
        Base repository with common functionality.
        @return A new unique identifier as a string.
        """
        return str(uuid.uuid4())