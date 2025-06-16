from fastapi import APIRouter
from pydantic import BaseModel
from database.models.robot import RobotRepository
from database.models.mission import Mission, MissionRepository
from database.models.block import Block, BlockRepository
from database.models.robot import Robot
from services.checker import checker
from typing import List

router = APIRouter()

class reqAddRobot(BaseModel):
    '''
    Class to define the request structure for adding a robot
    '''
    name: str = None

@router.post("/addrobot")
def route(req: reqAddRobot):
    '''
    Route to register a new robot
    '''
    try:
        db_robot = RobotRepository()
    
        db_robot.add(robot=Robot(
            id=db_robot.next_identity(),
            name=req.name
        ))
    
        return {
            "status": True
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }
    

class reqGetMission(BaseModel):
    '''
    Class to define the request structure
    '''
    robot_id: str = None

def getFullMission(mission: Mission, blocks: List[Block]):
    json_mission = mission.to_json()
    json_mission["blocks"] = [block.to_json() for block in blocks]

    return json_mission

@router.post("/getmissions")
def route(req: reqGetMission):
    '''
    Route that returns all missions of a robot
    '''
    try:
        db_mission = MissionRepository()
        db_block = BlockRepository()
        db_robot = RobotRepository()

        if not checker.checkObjectExists(db_robot, req.robot_id):
            raise Exception("Robot doesn't exists !")

        missions = db_mission.find_all_by_robot_id(req.robot_id)

        return {
            "status": True,
            "missions": [getFullMission(mission, db_block.find_many_by_mission_id(mission.id)) for mission in missions]
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }