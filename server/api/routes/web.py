from fastapi import APIRouter
from database.models.robot import RobotRepository
from database.models.robot import Robot, RobotId
from typing import Optional
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/addrobot")
def route(name: str, robot_id: Optional[str] = None):
    '''
    Route to register a new robot
    '''
    try:
        db_robot = RobotRepository()
    
        db_robot.add(robot=Robot(
            id=RobotId(id=robot_id) if ((robot_id != None) and (robot_id != "")) else db_robot.next_identity(),
            name=name
        ))
    
        return RedirectResponse(url=f"/?status={True}", status_code=303)
    except Exception as e:
        return RedirectResponse(url=f"/?status={False}", status_code=303)