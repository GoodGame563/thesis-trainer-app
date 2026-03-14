from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from models import Player, Team, Transfer

from .structs import Transfers


async def get_latest_transfer(
    async_session: async_sessionmaker[AsyncSession], player_id: int
) -> Transfer | None:
    return None
    # async with db_connect() as db:
    #     db.row_factory = aiosqlite.Row

    #     async with db.execute(
    #         """
    #         SELECT id, full_name, height, weight, date_birth, foto
    #         FROM players
    #         WHERE id = ?
    #     """,
    #         (player_id,),
    #     ) as cursor:
    #         player_row = await cursor.fetchone()
    #         if not player_row:
    #             return None

    #     player = Player(
    #         id=player_row["id"],
    #         full_name=player_row["full_name"],
    #         weight=float(player_row["weight"]),
    #         height=float(player_row["height"]),
    #         birth_date=date.fromisoformat(player_row["date_birth"]),
    #         path_to_photo=player_row["foto"],
    #     )

    #     async with db.execute(
    #         """
    #         SELECT tr.id, tr.date, t.id as team_id, t.name, t.logo
    #         FROM transfers tr
    #         JOIN teams t ON tr.team_id = t.id
    #         WHERE tr.player_id = ?
    #         ORDER BY tr.date DESC
    #         LIMIT 1
    #     """,
    #         (player_id,),
    #     ) as cursor:
    #         transfer_row = await cursor.fetchone()
    #         if not transfer_row:
    #             return None

    #     team = Team(
    #         id=transfer_row["team_id"],
    #         name=transfer_row["name"],
    #         path_to_logo=transfer_row["logo"],
    #     )

    #     transfer_date = date.fromisoformat(transfer_row["date"])

    #     return Transfer(
    #         id=transfer_row["id"], player=player, team=team, date=transfer_date
    #     )


async def create_transfer(
    async_session: async_sessionmaker[AsyncSession],
    player_id: int,
    team_id: int,
    transfer_date: date,
):
    async with async_session() as session, session.begin():
        session.add(Transfers(player_id, team_id, transfer_date))
