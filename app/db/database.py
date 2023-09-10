import motor.motor_asyncio

MONGO_URI = "mongodb://root:example@mongo:27017/"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client.dojo_otel
dojo_otel_collection = database.get_collection("dojo_otel_collection")

def collection_helper(data):
  return {
    "id": str(data["_id"]),
    "message": str(data["message"])
  }

async def read_db():
  read_data = []
  async for data in dojo_otel_collection.find():
    read_data.append(collection_helper(data))
  return read_data

async def write_db(write_data: dict):
  data = await dojo_otel_collection.insert_one(write_data)
  new_data = await dojo_otel_collection.find_one({"_id": data.inserted_id})
  return collection_helper(new_data)