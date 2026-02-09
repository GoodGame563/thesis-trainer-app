from typing import List
from models import Team
import aiosqlite
from .db_connection import db_connect

async def find_all_teams_by_user_id(player_id: int) ->List[Team]:
    async with db_connect() as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("""
                SELECT t.id, t.name, t.logo
                FROM all_games ag
                JOIN teams t ON ag.team_id = t.id
                WHERE ag.player_id = ?
            """, (player_id,)) as cursor:            
            teams = [Team(row['id'], row['name'], row['logo']) async for row in cursor]
    return teams
