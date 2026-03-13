from datetime import date

import aiosqlite

from models import Player, Team

from .db_connection import db_connect


async def get_player_with_roles_and_teams(player_id: int) -> dict | None:
    async with db_connect() as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM players WHERE id = ?", (player_id,)
        ) as cursor:
            player_row = await cursor.fetchone()
            if not player_row:
                return None
        player = Player(
            id=player_row["id"],
            birth_date=player_row["date_birth"],
            full_name=player_row["full_name"],
            height=player_row["height"],
            weight=player_row["weight"],
            path_to_photo=player_row["foto"],
        )

        async with db.execute(
            """
            SELECT t.id, t.name, t.logo
            FROM transfers tr
            JOIN teams t ON tr.team_id = t.id
            WHERE tr.player_id = ?
            ORDER BY tr.date DESC
            LIMIT 1
        """,
            (player_id,),
        ) as cursor:
            latest_row = await cursor.fetchone()
        current_team = (
            Team(
                id=latest_row["id"],
                name=latest_row["name"],
                path_to_logo=latest_row["logo"],
            )
            if latest_row
            else None
        )

        async with db.execute(
            """
            SELECT DISTINCT r.name as role, t.name as team
            FROM all_games ag
            JOIN roles r ON ag.role_id = r.id
            JOIN teams t ON ag.team_id = t.id
            WHERE ag.player_id = ?
        """,
            (player_id,),
        ) as cursor:
            roles_with_team = [dict(row) async for row in cursor]

        return {
            "player": player,
            "current_team": current_team,
            "roles_with_team": roles_with_team,
        }


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

    async with db_connect() as db:
        await db.execute(query, params)
        await db.commit()
        return db.total_changes > 0


async def get_all_players() -> list[Player]:
    async with db_connect() as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM players") as cursor:
            rows = await cursor.fetchall()
            return [
                Player(
                    id=row["id"],
                    birth_date=row["date_birth"],
                    full_name=row["full_name"],
                    height=row["height"],
                    weight=row["weight"],
                    path_to_photo=row["foto"],
                )
                for row in rows
            ]


async def create_player(player: Player):
    async with db_connect() as db:
        await db.execute(
            """INSERT INTO players (full_name, height, weight, date_birth, foto) VALUES (?, ?, ?, ?, ?)""",
            (
                player.full_name,
                player.height,
                player.weight,
                player.birth_date,
                player.path_to_photo,
            ),
        )
        await db.commit()
