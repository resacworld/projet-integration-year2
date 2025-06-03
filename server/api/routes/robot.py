from fastapi import APIRouter
from pydantic import BaseModel

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
    status_deplacement: bool = None
    orientation: float = None
    status_pince: bool = None
    timestamp: str = None

@router.post("/telemetry")
def register(req: reqTelemetry):
    '''
    Route to register the status of a robot's mission
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
