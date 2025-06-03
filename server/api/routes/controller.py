from fastapi import APIRouter

# router = APIRouter(prefix="/controller")
router = APIRouter()

@router.get("/todo")
def login():
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
