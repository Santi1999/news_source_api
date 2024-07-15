import os
from .config import settings

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure
from fastapi import HTTPException
from bson import ObjectId

class Database:
    def __init__(self, uri: str, db_name: str):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None

    async def connect(self):
        try:
            self.client = AsyncIOMotorClient(self.uri)
            # Ping the database to ensure connection is established
            await self.client.admin.command('ping')
            self.db = self.client[self.db_name]
        except ConnectionFailure as e:
            raise HTTPException(status_code=500, detail="Could not connect to the database")

    async def disconnect(self):
        if self.client:
            self.client.close()

uri = f"mongodb+srv://{settings.MONGO_USERNAME}:{settings.MONGO_PASS}@{settings.MONGO_HOST}/{settings.MONGO_DBNAME}?replicaSet={settings.REPLICA_SET}&tls={settings.TLS}&authSource={settings.AUTH_SOURCE}"
# Initialize the database instance
database = Database(uri=uri, db_name="newsArticles")


def object_id_str(value):
    if isinstance(value, ObjectId):
        return str(value)
    return value