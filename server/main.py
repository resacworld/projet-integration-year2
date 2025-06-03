from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Initialize the FastAPI application
app = FastAPI()


# Define the default route
@app.get("/", response_class=HTMLResponse)
async def root():
    return "<html><body><h1>Welcome to the FastAPI Server!</h1></body></html>"
