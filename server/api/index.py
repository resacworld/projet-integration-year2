from fastapi import APIRouter
from .routes.courses import router as coursesRouter
from .routes.robot import router as authRouter

# Create the master router
MasterRouter = APIRouter(prefix="/api")

# Include the child routers
MasterRouter.include_router(coursesRouter)
MasterRouter.include_router(authRouter)
