from database.interfaces.base import BaseObject, BaseIdentifier
from database.models.robot import RobotRepository
from typing import List

class checker:
    @staticmethod
    def checkObjectExists(db: RobotRepository, id: str | BaseIdentifier) -> bool:
        """
        Check if an object exists in the given database.
        """
        
        return db.find_by_id(id) is not None
    
    @staticmethod
    def isObjectInvalid(object: BaseObject) -> bool:
        """
        Check if an object is invalid (is None)
        """
        return object is None
    
    @staticmethod
    def isUniqueObjectsOnly(objects: List[object]):
        """
        Check if a list contains only unique instance of each objects
        """
        return len(objects) != len(set(objects))