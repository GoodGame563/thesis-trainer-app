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


async def get_all_teams() -> list[Team]:
    teams = []

    # async with db_connect() as db:
    #     db.row_factory = aiosqlite.Row
    #     async with db.execute(
    #         """
    #             SELECT id, name, logo
    #             FROM teams
    #         """,
    #     ) as cursor:
    #         teams = [Team(row["id"], row["name"], row["logo"]) async for row in cursor]
    return teams


async def create_teams(name: str, logo: str):
    pass
    # async with (
    #     db_connect() as db,
    #     db.execute(
    #         """
    #         INSERT INTO teams (name, logo)
    #         VALUES (?, ?)
    #     """,
    #         (name, logo),
    #     ),
    # ):
    #     await db.commit()
