from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)
database = client.mintmind

user_collection = database.get_collection("users")
report_collection = database.get_collection("reports")

# Create indexes
async def init_db():
    await user_collection.create_index("email", unique=True)
