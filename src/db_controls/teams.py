import aiosqlite
from sqlalchemy import select
from .structs import Teams, AllStats
from models import Team
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


async def find_all_teams_by_user_id(
    async_session: async_sessionmaker[AsyncSession], player_id: int
) -> list[Team]:
    teams = []
    async with async_session() as session:
        select_teams = (
            select(Teams)
            .select_from(AllStats)
            .join(Teams, Teams.id == AllStats.team_id)
            .where(AllStats.player_id == player_id)
            .distinct()
        )
        all_t = await session.execute(select_teams)
        for t in all_t.scalars():
            teams.append(t.to_model())
        print(teams)
    return teams


async def get_all_teams(async_session: async_sessionmaker[AsyncSession]) -> list[Team]:
    async with async_session() as session:
        result = (await session.execute(select(Teams))).scalars()
        return [t.to_model() for t in result]


async def create_teams(
    async_session: async_sessionmaker[AsyncSession], name: str, logo: str
):
    async with async_session() as session:
        async with session.begin():
            session.add(Teams(name, logo))
