from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI()


# Define the default route
@app.get("/")
async def root():
    return "<html><body><h1>Welcome to the FastAPI Server!</h1></body></html>"
