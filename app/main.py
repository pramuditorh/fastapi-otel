from fastapi import FastAPI, Depends
from config import get_settings, Settings
from api import read, write

app = FastAPI()

app.include_router(read.router)
app.include_router(write.router)

@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Hello World",
        "environment": settings.environment
    }