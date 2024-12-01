from databases import Database # type: ignore
from sqlalchemy import create_engine # type: ignore
from .config import settings

database = Database(settings.DATABASE_URL)

async def init_db():
    await database.connect()