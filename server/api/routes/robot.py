from fastapi import APIRouter

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

@router.post("/telemetry")
def register():
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

@router.post("/summary")
def register():
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
