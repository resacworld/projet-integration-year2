from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.index import MasterRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Initialize the FastAPI application
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # seulement si tu envoies des cookies ou auth headers
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# link the router to the fastapi instance
app.include_router(MasterRouter)

# Define the default route
@app.get("/", response_class=HTMLResponse)
async def root():
    with open('static/index.html', 'r') as file:
        return file.read()
