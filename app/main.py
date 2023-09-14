from fastapi import FastAPI, Depends
from app.config import get_settings, Settings
from app.api import read, write
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

app.include_router(read.router)
app.include_router(write.router)

@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Hello World",
        "environment": settings.environment
    }

FastAPIInstrumentor.instrument_app(app)