import os
from pymongo import AsyncMongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL=os.getenv("MONGODB_URI")



if not MONGO_DB_URL:
    raise ValueError("Database missing")

clt=AsyncMongoClient(MONGO_DB_URL)
db = clt["qble_db"]

async def db_connect():
    await clt.admin.command("ping")
    print("Mongo DB connected")



async def db_disconnect():
    await clt.close()
    print("Mongo DB connection failed")