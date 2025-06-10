from fastapi import APIRouter
from pydantic import BaseModel
from database.models.robotTelemetry import RobotTelemetryRepository, RobotTelemetry, RobotTelemetryId
from database.models.robot import RobotRepository, RobotId
from database.models.mission import Mission, MissionRepository
from database.models.block import Block, BlockRepository
from database.models.robot import Robot
from datetime import datetime

# router = APIRouter(prefix="/robot")
router = APIRouter()

@router.get("/instructions")
def route(robot_id: str = None):
    '''
    Route for the robot to get instructions
    
    '''

    try:
        db_robot = RobotRepository()
        db_mission = MissionRepository()
        db_block = BlockRepository()

        # Check if the robot exists, if not create it
        if(db_robot.find_by_id(robot_id) is None):
            raise Exception("Robot not found in the database. Please register the robot first.")
        
        current_mission = db_mission.find_by_robot_id_and_executing(robot_id, True)

        if current_mission != None:
            raise Exception("Robot already executing a mission !")
        
        mission = db_mission.find_next_mission_by_robot_id(robot_id)

        if(mission is None):
            raise Exception("No mission avalaible for this robot. Please add a mission first.")

        blocks = db_block.find_by_mission_id(mission.id)

        db_mission.update_execution_status(mission.id, executing=True)

        return {
            "status": True,
            "liste_blocks": [ block.block_nb for block in blocks ],
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }
    

class reqTelemetry(BaseModel):
    '''
    Class to define the request structure
    '''
    robot_id: str = None
    vitesse_instant: float = None
    ds_ultrasons: float = None
    status_deplacement: str = None
    orientation: float = None
    status_pince: bool = None
    # timestamp: str = None # => gérée par l'API (Cahier des Charges)

@router.post("/telemetry")
def route(req: reqTelemetry):
    '''
    Route to register the status of a robot's mission
    '''
    try:
        db_mission = MissionRepository()
        db_robot_telemetry = RobotTelemetryRepository()

        mission = db_mission.find_by_robot_id_and_executing(robot_id=req.robot_id, executing=True)

        if mission is None:
            raise Exception("No mission currently running for this robot. Please start a mission first.")

        db_robot_telemetry.add(
            RobotTelemetry(
                id=db_robot_telemetry.next_identity(),
                mission_id=mission.id,
                vitesse_instant=req.vitesse_instant,
                ds_ultrasons=req.ds_ultrasons,
                status_deplacement=req.status_deplacement,
                orientation=req.orientation,
                status_pince=req.status_pince,
                timestamp=datetime.now().isoformat()  # Automatically set the timestamp
            )
        )

        # Put instructions here
    
        return {
            "status": True
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }


class reqSummary(BaseModel):
    '''
    Class to define the request structure
    '''
    robot_id: str = None
    vitesse_moy: float = None
    tps_total: float = None

@router.post("/summary")
def route(req: reqSummary):
    '''
    Route to register the end of a robot's mission
    '''
    try:
        db_mission = MissionRepository()

        mission = db_mission.find_by_robot_id_and_executing(req.robot_id, executing=True)

        if mission is None:
            raise Exception("No mission currently running for this robot. Please start a mission first.")

        db_mission.update_execution_status(mission.id, executing=False, finished=True)

        return {
            "status": True,
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }
