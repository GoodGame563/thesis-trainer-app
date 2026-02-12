from typing import List

import aiosqlite

from models import Team

from .db_connection import db_connect


async def find_all_teams_by_user_id(player_id: int) -> list[Team]:
    async with db_connect() as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """
                SELECT t.id, t.name, t.logo
                FROM all_games ag
                JOIN teams t ON ag.team_id = t.id
                WHERE ag.player_id = ?
            """,
            (player_id,),
        ) as cursor:
            teams = [Team(row["id"], row["name"], row["logo"]) async for row in cursor]
    return teams


async def get_all_teams() -> list[Team]:
    async with db_connect() as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """
                SELECT id, name, logo
                FROM teams
            """,
        ) as cursor:
            teams = [Team(row["id"], row["name"], row["logo"]) async for row in cursor]
    return teams

async def create_teams(name:str, logo:str):
    async with db_connect() as db:
        async with db.execute(
            """
            INSERT INTO teams (name, logo)
            VALUES (?, ?)
        """,
            (name, logo),
        ):
            await db.commit()