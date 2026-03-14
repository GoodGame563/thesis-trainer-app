from os import makedirs, path

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from models import Role

from .structs import Base, Roles

data_path = "data"
db_path = f"{data_path}/base.db"


async def create_db():
    if not path.exists(data_path):
        makedirs(data_path)
    engine = create_async_engine("sqlite+aiosqlite:///" + db_path, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_sessionmaker(engine, expire_on_commit=False)() as session:
        if (await session.execute(select(Roles).limit(1))).one_or_none() is None:
            for role in Role:
                session.add(Roles(name=role.name))
            await session.commit()
    return engine
