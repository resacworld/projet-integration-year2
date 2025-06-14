from fastapi import APIRouter
from pydantic import BaseModel
from database.models.robot import RobotRepository, RobotId
from database.models.mission import MissionRepository, Mission
from database.models.block import BlockRepository, Block
from database.models.robotTelemetry import RobotTelemetryRepository, RobotTelemetry
from typing import List

# router = APIRouter(prefix="/controller")
router = APIRouter()

# class reqBlock(BaseModel):
#     '''
#     Class to define the structure of a block in a mission
#     '''
#     block_nb: int = None

class reqAddMission(BaseModel):
    '''
    Class to define the request structure
    '''
    robot_id: str = None
    name: str = None
    blocks: List[int] = None

@router.post("/addmission")
def route(req: reqAddMission):
    '''
    Route to implement
    '''
    try:
        db_robot = RobotRepository()
        db_mission = MissionRepository()
        db_block = BlockRepository()

        if len(req.blocks) == 0:
            raise Exception("No blocks provided for the mission. Please add at least one block.")
        
        if db_robot.find_by_id(req.robot_id) is None:
            raise Exception("Robot not found in the database. Please register the robot first.")
        
        if len(req.blocks) != len(set(req.blocks)):
            raise Exception("Double block found in the sequence !!")

        mission_id = db_mission.next_identity()
    
        db_mission.add(mission=Mission(
            id=mission_id,
            robot_id=RobotId(id=req.robot_id),
            name=req.name,
            finished=False,
            executing=False
        ))

        i = 0
        for block in req.blocks:
            db_block.add(block=Block(
                id=db_block.next_identity(),
                mission_id=mission_id,
                block_nb=block,
                block_order=i
            ))

            i+=1

        return {
            "status": True
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }

class reqLastTelemety(BaseModel):
    '''
    Class to define the request structure
    '''
    robot_id: str = None

@router.post("/lasttelemetry")
def route(req: reqLastTelemety):
    '''
    Route to implement
    '''
    try:
        db_robot_telemetry = RobotTelemetryRepository()
        db_mission = MissionRepository()

        print(req.robot_id)

        mission = db_mission.find_by_robot_id_and_executing(req.robot_id, executing=True)

        if mission == None:
            raise Exception("No active mission find")

        telemetry: RobotTelemetry = db_robot_telemetry.find_last_by_mission_id(mission_id=mission.id)

        # Put instructions here

        return {
            "status": True,
            "telemetry": telemetry.to_json() if telemetry != None else None
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }

@router.get("/robots")
def route():
    '''
    Route to implement
    '''
    try:
        db_robot = RobotRepository()

        robots = db_robot.find_all()

        # Put instructions here

        return {
            "status": True,
            "robots": [robot.to_json() for robot in robots]
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }