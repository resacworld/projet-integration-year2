from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.index import MasterRouter
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

@app.get("/", response_class=HTMLResponse)
async def homepage(status: bool = None, selected_id: str = None):
    return getFullHomePage(status=status, selected_id=selected_id)