# import motor.motor_asyncio
import pymongo
from opentelemetry.instrumentation.pymongo import PymongoInstrumentor

MONGO_URI = "mongodb://root:example@mongo:27017/"

PymongoInstrumentor().instrument()

client = pymongo.MongoClient(MONGO_URI)
database = client.dojo_otel
dojo_otel_collection = database.dojo_otel_collection  # Use the collection directly

def collection_helper(data):
    return {
        "id": str(data["_id"]),
        "message": str(data["message"])
    }

def read_db():
    read_data = []
    cursor = dojo_otel_collection.find()
    for data in cursor:
        read_data.append(collection_helper(data))
    return read_data

def write_db(write_data: dict):
    result = dojo_otel_collection.insert_one(write_data)
    new_data = dojo_otel_collection.find_one({"_id": result.inserted_id})
    return collection_helper(new_data)