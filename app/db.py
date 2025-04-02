from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

sqlite_file_name = "url_short.db"

sync_engine = create_engine(f"sqlite:///{sqlite_file_name}")

async_engine = create_async_engine(f"sqlite+aiosqlite:///{sqlite_file_name}")


def create_db_and_tables():
    SQLModel.metadata.create_all(sync_engine)






