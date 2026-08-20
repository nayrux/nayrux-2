import motor.motor_asyncio
import os
from config import Config

class Database:
    def __init__(self):
        self.client = None
        self.db = None
    
    async def connect(self):
        if Config.DATABASE_URL:
            # MongoDB (Recomendado para Railway)
            self.client = motor.motor_asyncio.AsyncIOMotorClient(Config.DATABASE_URL)
            self.db = self.client.get_default_database()
            print("✅ Conectado a MongoDB")
        else:
            print("⚠️ Usando modo sin base de datos (configura DATABASE_URL)")
    
    async def get_user_data(self, user_id, guild_id):
        if not self.db:
            return {}
        collection = self.db.economy
        return await collection.find_one({"user_id": user_id, "guild_id": guild_id})
    
    async def update_user_data(self, user_id, guild_id, data):
        if not self.db:
            return
        collection = self.db.economy
        await collection.update_one(
            {"user_id": user_id, "guild_id": guild_id},
            {"$set": data},
            upsert=True
        )

db = Database()