from datetime import date

import aiosqlite

from models import KpiRole, Player, Role, ShortTableData, TableData, Team

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
            g.minutes_played,
            g.passes_accurate,
            g.passes_inaccurate,
            g.passes_percent,
            g.captures_done,
            g.captures_missed,
            g.captures_percent,
            g.rakov_cleared,
            g.tackles_done,
            g.meters_covered,
            g.defenders_beaten,
            g.breakthroughs,
            g.attempts_grounded,
            g.realizations_scored,
            g.realizations_attempted,
            g.realizations_percent,
            g.penalties_scored,
            g.penalties_attempted,
            g.penalties_percent,
            g.dropgoals_scored,
            g.dropgoals_attempted,
            g.dropgoals_percent,
            g.points_scored,
            g.penalties_received,
            g.loss_ball,
            g.yellow_cards,
            g.red_cards
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
                    passes_accurate=row["passes_accurate"],
                    passes_inaccurate=row["passes_inaccurate"],
                    passes_percent=row["passes_percent"],
                    captures_done=row["captures_done"],
                    captures_missed=row["captures_missed"],
                    captures_percent=row["captures_percent"],
                    rakov_cleared=row["rakov_cleared"],
                    tackles_done=row["tackles_done"],
                    meters_covered=row["meters_covered"],
                    defenders_beaten=row["defenders_beaten"],
                    breakthroughs=row["breakthroughs"],
                    attempts_grounded=row["attempts_grounded"],
                    realizations_scored=row["realizations_scored"],
                    realizations_attempted=row["realizations_attempted"],
                    realizations_percent=row["realizations_percent"],
                    penalties_scored=row["penalties_scored"],
                    penalties_attempted=row["penalties_attempted"],
                    penalties_percent=row["penalties_percent"],
                    dropgoals_scored=row["dropgoals_scored"],
                    dropgoals_attempted=row["dropgoals_attempted"],
                    dropgoals_percent=row["dropgoals_percent"],
                    points_scored=row["points_scored"],
                    penalties_received=row["penalties_received"],
                    loss_ball=row["loss_ball"],
                    yellow_cards=row["yellow_cards"],
                    red_cards=row["red_cards"],
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
                    passes_accurate=row["passes_accurate"],
                    passes_inaccurate=row["passes_inaccurate"],
                    passes_percent=row["passes_percent"],
                    captures_done=row["captures_done"],
                    captures_missed=row["captures_missed"],
                    captures_percent=row["captures_percent"],
                    rakov_cleared=row["rakov_cleared"],
                    tackles_done=row["tackles_done"],
                    meters_covered=row["meters_covered"],
                    defenders_beaten=row["defenders_beaten"],
                    breakthroughs=row["breakthroughs"],
                    attempts_grounded=row["attempts_grounded"],
                    realizations_scored=row["realizations_scored"],
                    realizations_attempted=row["realizations_attempted"],
                    realizations_percent=row["realizations_percent"],
                    penalties_scored=row["penalties_scored"],
                    penalties_attempted=row["penalties_attempted"],
                    penalties_percent=row["penalties_percent"],
                    dropgoals_scored=row["dropgoals_scored"],
                    dropgoals_attempted=row["dropgoals_attempted"],
                    dropgoals_percent=row["dropgoals_percent"],
                    points_scored=row["points_scored"],
                    penalties_received=row["penalties_received"],
                    loss_ball=row["loss_ball"],
                    yellow_cards=row["yellow_cards"],
                    red_cards=row["red_cards"],
                    rating=0.0,
                )
                result.append(table_data)

    return result
