"""
AI helped in writing the comments
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.index import MasterRouter, MasterRouterAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pages.home import getFullHomePage

# Initialize the FastAPI application
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# link the router to the fastapi instance
app.include_router(MasterRouter)
app.include_router(MasterRouterAPI)

@app.get("/", response_class=HTMLResponse)
async def homepage(status: bool = None, selected_id: str = None):
    """!
    Route to return the html home page
    @param status: Status of the last operation (True for success, False for error)
    @param selected_id: ID of the selected robot
    @return home page as HTML response
    """

    return getFullHomePage(status=status, selected_id=selected_id)