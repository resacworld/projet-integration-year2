"""
AI helped in writing the comments
"""

from database.interfaces.base import BaseObject, BaseIdentifier
from database.models.robot import RobotRepository
from typing import List

class checker:
    @staticmethod
    def checkObjectExists(db: RobotRepository, id: str | BaseIdentifier) -> bool:
        """!
        Check if an object exists in the given database.
        @param db: Database repository to check the object in
        @param id: ID of the object to check
        @return True if the object exists, False otherwise
        """
        
        return db.find_by_id(id) is not None
    
    @staticmethod
    def isObjectInvalid(object: BaseObject) -> bool:
        """!
        Check if an object is invalid (is None)
        @param object: The object to check
        @return True if the object is invalid, False otherwise
        """
        return object is None
    
    @staticmethod
    def isUniqueObjectsOnly(objects: List[object]):
        """!
        Check if a list contains only unique instance of each objects
        @param objects: List of objects to check
        @return True if the list contains only unique objects, False otherwise
        """
        return len(objects) != len(set(objects))