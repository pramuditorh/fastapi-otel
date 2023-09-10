from pydantic import BaseModel, Field

class DataSchema(BaseModel):
  message: str = Field(...)

  class Config:
    schema_extra = {
      "example": {
        "message": "This is an example"
      }
    }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}