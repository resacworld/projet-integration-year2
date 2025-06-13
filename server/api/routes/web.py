from fastapi import APIRouter
from pydantic import BaseModel
from database.models.robot import RobotRepository
from database.models.mission import Mission, MissionRepository
from database.models.block import BlockRepository
from database.models.robot import Robot

# router = APIRouter(prefix="/web")
router = APIRouter()

class reqAddRobot(BaseModel):
    '''
    Class to define the request structure for adding a robot
    '''
    mac: str = None
    name: str = None

@router.post("/addrobot")
def route(req: reqAddRobot):
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

@router.post("/getmissions")
def route(req: reqGetMission):
    '''
    Route to implement
    '''
    try:
        db_mission = MissionRepository()
        db_block = BlockRepository()

        missions = db_mission.find_all_by_robot_id(req.robot_id)

        def getFullMission(mission: Mission):
            json_mission = mission.to_json()
            json_mission["blocks"] = db_block.find_by_mission_id(mission.id)

            return json_mission

        return {
            "status": True,
            "missions": [getFullMission(mission) for mission in missions]
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }