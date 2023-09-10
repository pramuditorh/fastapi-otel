from fastapi import APIRouter
from app.db.database import read_db
from app.models.data import ResponseModel

router = APIRouter()

@router.get("/read")
async def get_data():
    data = await read_db()
    if data:
        return ResponseModel(data, "Data sucessfully retrieve")
    return ResponseModel(data, "Empty data")