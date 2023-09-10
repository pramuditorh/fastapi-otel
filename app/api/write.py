from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.db.database import write_db
from app.models.data import ResponseModel, DataSchema

router = APIRouter()

@router.post("/write")
async def add_data(data: DataSchema = Body(...)):
    data = jsonable_encoder(data)
    new_data = await write_db(data)
    return ResponseModel(new_data, "Data successfully added")