from fastapi import APIRouter

router = APIRouter(prefix="/robot")


@router.get("/instructions")
def login():
    '''
    Route for the robot to get instructions
    '''
    try:
        return NotImplementedError
    
        # Put instructions here
    
        return {
            "status": True,
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }

@router.post("/status")
def register():
    '''
    Route to register the status of a robot's mission
    '''
    try:
        return NotImplementedError
    
        # Put instructions here
    
        return {
            "status": True,
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }

@router.post("/end")
def register():
    '''
    Route to register the end of a robot's mission
    '''
    try:
        return NotImplementedError

        # Put instructions here

        return {
            "status": True,
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }
