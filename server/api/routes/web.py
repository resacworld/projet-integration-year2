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

@router.get("/addrobot")
def register():
    '''
    Route to register the status of a robot's mission
    '''
    try:
        db_robot = RobotRepository()
        
        robot_id = db_robot.next_identity()

        db_robot.add(robot=Robot(
            id=robot_id,
            mac="NO MAC ENTERED",
            name="Robot 1"
        ))

        # Put instructions here
    
        return {
            "robot_id": robot_id.id,
            "status": True
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }