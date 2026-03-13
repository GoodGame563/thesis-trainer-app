from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from .structs import Players, Teams, Transfers, Roles, AllStats
from models import Player, Team
from datetime import date


async def get_player(
    async_session: async_sessionmaker[AsyncSession], player_id: int
) -> Player:
    async with async_session() as session:
        select_pl = select(Players).where(Players.id == player_id)
        player = (await session.execute(select_pl)).scalar_one()
        return player.to_model()


async def get_players_team(
    async_session: async_sessionmaker[AsyncSession], player_id: int
) -> Team | None:
    async with async_session() as session:
        select_team = (
            select(Teams)
            .select_from(Transfers)
            .join(Teams)
            .where(Transfers.player_id == player_id)
            .order_by(Transfers.date)
            .limit(1)
        )
        current_team = (await session.execute(select_team)).scalar()
        if current_team is None:
            return None
        return current_team.to_model()


async def get_players_roles_and_teams(
    async_session: async_sessionmaker[AsyncSession], player_id: int
) -> list[tuple[str, str]] | None:
    async with async_session() as session:
        roles_with_team = []

        all_r = (
            select(Roles.name, Teams.name)
            .select_from(AllStats)
            .join(Roles, AllStats.role_id == Roles.id)
            .join(Teams, AllStats.team_id == Teams.id)
            .where(AllStats.player_id == player_id)
        )

        find_all_r = (await session.execute(all_r)).tuples()

        for r in find_all_r:
            roles_with_team.append(r)
        return roles_with_team


async def update_player(
    player_id: int,
    full_name: str | None = None,
    height: int | None = None,
    weight: int | None = None,
    date_birth: date | None = None,
) -> bool:
    updates = []
    params = []

    if full_name is not None:
        updates.append("full_name = ?")
        params.append(full_name)
    if height is not None:
        updates.append("height = ?")
        params.append(height)
    if weight is not None:
        updates.append("weight = ?")
        params.append(weight)
    if date_birth is not None:
        updates.append("date_birth = ?")
        params.append(date_birth)

    if not updates:
        return False

    params.append(player_id)
    query = f"UPDATE players SET {', '.join(updates)} WHERE id = ?"
    return True

    # async with db_connect() as db:
    #     await db.execute(query, params)
    #     await db.commit()
    #     return db.total_changes > 0


async def get_all_players() -> list[Player]:
    return []
    # async with db_connect() as db:
    #     db.row_factory = aiosqlite.Row
    #     async with db.execute("SELECT * FROM players") as cursor:
    #         rows = await cursor.fetchall()
    #         return [
    #             Player(
    #                 id=row["id"],
    #                 birth_date=row["date_birth"],
    #                 full_name=row["full_name"],
    #                 height=row["height"],
    #                 weight=row["weight"],
    #                 path_to_photo=row["foto"],
    #             )
    #             for row in rows
    #         ]


async def create_player(player: Player):
    pass
    # async with db_connect() as db:
    #     await db.execute(
    #         """INSERT INTO players (full_name, height, weight, date_birth, foto) VALUES (?, ?, ?, ?, ?)""",
    #         (
    #             player.full_name,
    #             player.height,
    #             player.weight,
    #             player.birth_date,
    #             player.path_to_photo,
    #         ),
    #     )
    #     await db.commit()
