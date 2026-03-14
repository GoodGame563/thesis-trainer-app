import aiosqlite
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

engine = None


def set_engine(out_engine: AsyncEngine):
    global engine
    engine = out_engine


def get_session():
    return async_sessionmaker(engine, expire_on_commit=False)

    # return create_async_engine("sqlite+aiosqlite:///"+db_path, echo=True)
