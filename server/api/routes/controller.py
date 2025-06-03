from fastapi import APIRouter
import src.main as configs
from ...database.postgres.models import User

router = APIRouter(prefix="/controller")


@router.post("/todo")
def login(user: User):
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


@router.put("/todo2")
def register(user: User):
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
