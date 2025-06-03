from fastapi import APIRouter
from pydantic import BaseModel
from database.models.robotTelemetry import RobotTelemetryRepository, RobotTelemetry, RobotTelemetryId
from datetime import datetime

# router = APIRouter(prefix="/robot")
router = APIRouter()

@router.get("/instructions")
def login():
    '''
    Route for the robot to get instructions
    '''
    try:

        # Put instructions here
    
        return {
            "status": True,
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
    vitesse_instant: float = None
    ds_ultrasons: float = None
    status_deplacement: str = None
    orientation: float = None
    status_pince: bool = None
    # timestamp: str = None # => gérée par l'API (Cahier des Charges)

@router.post("/telemetry")
def register(req: reqTelemetry):
    '''
    Route to register the status of a robot's mission
    '''
    try:

        RobotTelemetryRepository().add(
            RobotTelemetry(
                id=RobotTelemetryId(id=""),
                robotid="robot1",  # This should be dynamically set based on the robot's mac address
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
    vitesse_moy: float = None
    tps_total: float = None

@router.post("/summary")
def register(req: reqSummary):
    '''
    Route to register the end of a robot's mission
    '''
    try:

        # Put instructions here

        return {
            "status": True,
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }
