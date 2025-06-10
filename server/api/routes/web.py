from fastapi import APIRouter
from pydantic import BaseModel
from database.models.robotTelemetry import RobotTelemetryRepository, RobotTelemetry, RobotTelemetryId
from database.models.robot import RobotRepository
from database.models.mission import Mission, MissionRepository
from database.models.block import Block, BlockRepository
from database.models.robot import Robot
from datetime import datetime
import json

# router = APIRouter(prefix="/web")
router = APIRouter()

class reqAddRobot(BaseModel):
    '''
    Class to define the request structure for adding a robot
    '''
    mac: str = None
    name: str = None

@router.post("/addrobot")
def register(req: reqAddRobot):
    '''
    Route to register the status of a robot's mission
    '''
    try:
        db_robot = RobotRepository()
    
        db_robot.add(robot=Robot(
            id=db_robot.next_identity(),
            mac=req.mac,
            name=req.name
        ))

        # Put instructions here
    
        return {
            "status": True
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }