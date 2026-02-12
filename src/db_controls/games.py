from datetime import date

import aiosqlite

from models import Player, Role, ShortTableData, TableData, Team

from .db_connection import db_connect


async def get_games_statistics() -> list[TableData]:
    query = """
        SELECT
            p.id as pl_id,
            p.full_name,
            p.weight,
            p.height,
            p.date_birth,
            p.foto,
            t.id as t_id,
            t.name as command,
            t.logo,
            r.name as role,
            g.*
        FROM all_games g
        JOIN players p ON g.player_id = p.id
        JOIN teams t ON g.team_id = t.id
        JOIN roles r ON g.role_id = r.id
        ORDER BY g.id
    """

    result = []
    async with db_connect() as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query) as cursor:
            async for row in cursor:
                birth_date = date.fromisoformat(row["date_birth"])

                Team(id=row["t_id"], name=row["command"], path_to_logo=row["logo"])

                player = Player(
                    id=row["pl_id"],
                    full_name=row["full_name"],
                    weight=row["weight"],
                    height=row["height"],
                    birth_date=birth_date,
                    path_to_photo=row["foto"],
                )

                role = Role[row["role"]]

                rating = 0.0

                table_data = TableData(
                   player=player,
                    role=role,
                    date_birth=birth_date,
                    team=row["command"],
                    minutes_played=row["minutes_played"],
                    successful_passes=row["successful_passes"],
                    bad_passes=row["bad_passes"],
                    successful_tackle=row["successful_tackle"],
                    dominant_tackles=row["dominant_tackles"],
                    miss_tackle=row["miss_tackle"],
                    ruck_cleared=row["ruck_cleared"],
                    steals=row["steals"],
                    metres_carried=row["metres_carried"],
                    defenders_beaten=row["defenders_beaten"],
                    carriers=row["carriers"],
                    line_breaks=row["line_breaks"],
                    line_break_assists=row["line_break_assists"],
                    tries=row["tries"],
                    try_assists=row["try_assists"],
                    successful_conversions=row["successful_conversions"],
                    miss_conversions=row["miss_conversions"],
                    successful_penalties=row["successful_penalties"],
                    miss_penalties=row["miss_penalties"],
                    successful_drop_goal=row["successful_drop_goal"],
                    miss_drop_goal=row["miss_drop_goal"],
                    points=row["points"],
                    scrums_win=row["scrums_win"],
                    scrums_steal=row["scrums_steal"],
                    scrums_lose=row["scrums_lose"],
                    lineout_win=row["lineout_win"],
                    lineout_steal=row["lineout_steal"],
                    lineout_lose=row["lineout_lose"],
                    ball_losses=row["ball_losses"],
                    penalty=row["penalty"],
                    yellow_card=row["yellow_card"],
                    red_card=row["red_card"],
                    rating=rating,
                )
                result.append(table_data)

    return result


async def get_all_games_by_player_team_id(
    player_id: int, team_id: int
) -> list[ShortTableData]:
    query = """
               SELECT
            g.*,
			r.name as role
        FROM all_games g
		JOIN roles r on g.role_id = r.id
        WHERE g.player_id = ? AND g.team_id = ?
        ORDER BY g.id
    """

    result = []
    async with db_connect() as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query, (player_id, team_id)) as cursor:
            async for row in cursor:
                table_data = ShortTableData(
                    role=Role[row["role"]],
                    minutes_played=row["minutes_played"],
                    successful_passes=row["successful_passes"],
                    bad_passes=row["bad_passes"],
                    successful_tackle=row["successful_tackle"],
                    dominant_tackles=row["dominant_tackles"],
                    miss_tackle=row["miss_tackle"],
                    ruck_cleared=row["ruck_cleared"],
                    steals=row["steals"],
                    metres_carried=row["metres_carried"],
                    defenders_beaten=row["defenders_beaten"],
                    carriers=row["carriers"],
                    line_breaks=row["line_breaks"],
                    line_break_assists=row["line_break_assists"],
                    tries=row["tries"],
                    try_assists=row["try_assists"],
                    successful_conversions=row["successful_conversions"],
                    miss_conversions=row["miss_conversions"],
                    successful_penalties=row["successful_penalties"],
                    miss_penalties=row["miss_penalties"],
                    successful_drop_goal=row["successful_drop_goal"],
                    miss_drop_goal=row["miss_drop_goal"],
                    points=row["points"],
                    scrums_win=row["scrums_win"],
                    scrums_steal=row["scrums_steal"],
                    scrums_lose=row["scrums_lose"],
                    lineout_win=row["lineout_win"],
                    lineout_steal=row["lineout_steal"],
                    lineout_lose=row["lineout_lose"],
                    ball_losses=row["ball_losses"],
                    penalty=row["penalty"],
                    yellow_card=row["yellow_card"],
                    red_card=row["red_card"],
                    rating=0.0,
                )
                result.append(table_data)

    return result
