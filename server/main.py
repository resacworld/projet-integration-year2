from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.index import MasterRouter

# Initialize the FastAPI application
app = FastAPI()

# link the router to the fastapi instance
app.include_router(MasterRouter)

# Define the default route
@app.get("/", response_class=HTMLResponse)
async def root():
    with open('pages/main.html', 'r') as file:
        return file.read()
