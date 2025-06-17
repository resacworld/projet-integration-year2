from fastapi import APIRouter
from .routes.robot import router as robotRouter
from .routes.controller import router as controllerRouter
from .routes.web import router as webRouter

# Create the master router
MasterRouter = APIRouter()
MasterRouterAPI = APIRouter(prefix="/api")

# Include the child routers
MasterRouter.include_router(robotRouter)
MasterRouterAPI.include_router(controllerRouter)
MasterRouterAPI.include_router(webRouter)
