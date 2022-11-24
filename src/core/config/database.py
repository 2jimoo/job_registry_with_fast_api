from motor.motor_asyncio import AsyncIOMotorClient

from odmantic import AIOEngine
from src.core.config.config import Config

DB_URI = Config.mongodb_uri
DB_NAME = Config.app_name
client = AsyncIOMotorClient(DB_URI)
engine = AIOEngine(client=client, database=DB_NAME)


class MongoDB:
    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        self.client = client
        self.engine = engine
        print("Connected to DB")

    def close(self):
        self.client.close()


mongodb = MongoDB()
