from motor.motor_asyncio import AsyncIOMotorClient
import os

# Create mongo client using url
client = AsyncIOMotorClient(os.getenv("MONGO_URL"))

# Connect to your db
DB = client["ai-document-summarizer"]

print("DB Connected !")