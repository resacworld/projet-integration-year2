from fastapi import APIRouter
from .routes.robot import router as robotRouter
from .routes.controller import router as controllerRouter

# Create the master router
MasterRouter = APIRouter(prefix="/api")

# Include the child routers
MasterRouter.include_router(robotRouter)
MasterRouter.include_router(controllerRouter)
