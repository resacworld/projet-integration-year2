from fastapi import APIRouter
from pydantic import BaseModel

# router = APIRouter(prefix="/controller")
router = APIRouter()

class req(BaseModel):
    '''
    Class to define the request structure
    '''
    status: bool = False
    error: str = None

@router.post("/addmission")
def login(req: req):
    '''
    Route to implement
    '''
    try:
        print(req.status)
    
        # Put instructions here

        return {
            "status": True
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }


@router.put("/todo2")
def register():
    '''
    Route to implement
    '''
    try:
        return NotImplementedError
    
        # Put instructions here

        return {
            "status": True
        }
    except Exception as e:
        return {
            "status": False,
            "error": str(e)
        }
