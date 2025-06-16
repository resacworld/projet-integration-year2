from fastapi import APIRouter
from pydantic import BaseModel
from database.models.robotTelemetry import RobotTelemetryRepository, RobotTelemetry
from database.models.robot import RobotRepository
from database.models.mission import MissionRepository
from database.models.block import BlockRepository
from datetime import datetime
from services.checker import checker

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

        # Check if the robot exists
        if not checker.checkObjectExists(db_robot, robot_id):
            raise Exception("Robot not found in the database. Please register the robot first.")
        
        current_mission = db_mission.find_by_robot_id_and_executing(robot_id, executing=True)

        if current_mission != None:
            raise Exception("Robot already executing a mission !")
        
        mission = db_mission.find_next_mission_by_robot_id(robot_id)

        if checker.isObjectInvalid(mission):
            raise Exception("No mission available for this robot. Please add a mission first.")

        blocks = db_block.find_many_by_mission_id(mission.id)

        db_mission.start_mission(mission.id)

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
    vitesse: float = None
    distance_ultrasons: float = None
    statut_deplacement: str = None
    ligne: int = None
    status_pince: bool = None
    # timestamp: str = None # => gérée par l'API (Cahier des Charges)

@router.post("/telemetry")
def route(req: reqTelemetry):
    '''
    Route to register the status of a robot's mission (register a telemetry)
    '''
    try:
        db_mission = MissionRepository()
        db_robot_telemetry = RobotTelemetryRepository()
        db_robot = RobotRepository()

        # Check if the robot exists
        if not checker.checkObjectExists(db_robot, req.robot_id):
            raise Exception("Robot not found in the database. Please register the robot first.")

        mission = db_mission.find_by_robot_id_and_executing(robot_id=req.robot_id, executing=True)

        if checker.isObjectInvalid(mission):
            raise Exception("No mission currently running for this robot. Please start a mission first.")

        db_robot_telemetry.add(
            RobotTelemetry(
                id=db_robot_telemetry.next_identity(),
                mission_id=mission.id,
                vitesse_instant=req.vitesse,
                ds_ultrasons=req.distance_ultrasons,
                status_deplacement=req.statut_deplacement,
                ligne=req.ligne,
                status_pince=req.status_pince,
                timestamp=datetime.now().isoformat()  # Automatically set the timestamp
            )
        )
    
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

        # TODO: check if robot exists

        mission = db_mission.find_by_robot_id_and_executing(req.robot_id, executing=True)

        if checker.isObjectInvalid(mission):
            raise Exception("No mission currently running for this robot. Please start a mission first.")

        db_mission.end_mission(mission.id)

        return {
            "status": True,
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }
