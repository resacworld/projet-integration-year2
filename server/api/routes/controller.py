from fastapi import APIRouter
from pydantic import BaseModel
from database.models.robot import RobotRepository, RobotId
from database.models.mission import MissionRepository, Mission
from database.models.block import BlockRepository, Block
from typing import List

# router = APIRouter(prefix="/controller")
router = APIRouter()

class reqBlock(BaseModel):
    '''
    Class to define the structure of a block in a mission
    '''
    block_nb: int = None
    status_pince: bool = None

class reqAddMission(BaseModel):
    '''
    Class to define the request structure
    '''
    robot_id: str = None
    name: str = None
    # nb_blocks: int = None,
    blocks: List[reqBlock] = None

@router.post("/addmission")
def login(req: reqAddMission):
    '''
    Route to implement
    '''
    try:
        db_robot = RobotRepository()
        db_mission = MissionRepository()
        db_block = BlockRepository()

        if(len(req.blocks) == 0):
            raise Exception("No blocks provided for the mission. Please add at least one block.")
        
        if(db_robot.find_by_id(req.robot_id) is None):
            raise Exception("Robot not found in the database. Please register the robot first.")

        mission_id = db_mission.next_identity()
    
        db_mission.add(mission=Mission(
            id=mission_id,
            robot_id=RobotId(id=req.robot_id),
            name=req.name,
            nb_blocks=99999,  #TODO: remove useless field : req.nb_blocks,
            finished=False,
            executing=False
        ))

        for block in req.blocks:
            db_block.add(block=Block(
                id=db_block.next_identity(),
                mission_id=mission_id,
                block_nb=block.block_nb,
                status_pince=block.status_pince
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
    currently_running: bool = None

@router.post("/getmission")
def register(req: reqGetMission):
    '''
    Route to implement
    '''
    try:
        db_mission = MissionRepository()

        mission = db_mission.find_by_robot_id_and_executing(req.robot_id, req.currently_running)

        # Put instructions here

        return {
            "status": True,
            "mission": mission.to_json() if mission else None
        }
    except Exception as e:
        raise e
        return {
            "status": False,
            "error": str(e)
        }
