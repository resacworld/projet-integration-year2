from fastapi import APIRouter
from pydantic import BaseModel
from database.models.robot import RobotRepository
from database.models.mission import MissionRepository, Mission
from database.models.block import BlockRepository

# router = APIRouter(prefix="/simulator")
router = APIRouter()

# db_robot = RobotRepository()
# db_mission = MissionRepository()
# db_block = BlockRepository()

# class req(BaseModel):
#     '''
#     Class to define the request structure
#     '''
#     status: bool = False
#     error: str = None

# @router.post("/todo1")
# def login(req: req):
#     '''
#     Route to implement
#     '''
#     try:
#         print(req.status)

#         return NotImplementedError
    
#         # Put instructions here

#         return {
#             "status": True
#         }
#     except Exception as e:
#         return {
#             "status": False,
#             "error": str(e)
#         }


# @router.put("/todo2")
# def register():
#     '''
#     Route to implement
#     '''
#     try:
#         return NotImplementedError
    
#         # Put instructions here

#         return {
#             "status": True
#         }
#     except Exception as e:
#         return {
#             "status": False,
#             "error": str(e)
#         }
