from datetime import date

from models import Player, Role, TableData, Team
import aiosqlite
from .db_connection import db_connect


async def get_games_statistics() -> list[TableData]:
    ROLE_MAPPING = {
        "First line": Role.FIRST_LINE,
        "Second line": Role.SECOND_LINE,
        "Third line": Role.THIRD_LINE,
        "Scrum-half": Role.SCRUM_HALF,
        "Fly-half": Role.FLY_HALF,
        "Center": Role.CENTER,
        "Wing": Role.WING,
        "Fullback": Role.FULLBACK,
        "Nothing": Role.NOTHING,
    }

    query = """
        SELECT
            p.full_name,
            p.weight,
            p.height,
            p.date_birth,
            p.foto,
            t.name,
            t.logo,
            r.name,
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
        LIMIT 30
    """

    # await cur.execute(query)
    # rows = await cur.fetchall()
    # conn.close()

    result = []
    async with db_connect() as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(query) as cursor:
            async for row in cursor:
                birth_date = date.fromisoformat(row['date_birth'])

                team = Team(name=row['name'], path_to_logo=row['logo'])

                player = Player(
                    nst=row['full_name'],
                    weight=row['weight'],
                    height=row['height'],
                    team=team,
                    birth_date=birth_date,
                    path_to_photo=row['foto'],
                )

                role = ROLE_MAPPING.get(row[7], Role.NOTHING)

                rating = 0.0

                table_data = TableData(
                    player=player,
                    role=role,
                    minutes_played=row['minutes_played'],
                    passes_accurate=row['passes_accurate'],
                    passes_inaccurate=row['passes_inaccurate'],
                    passes_percent=row['passes_percent'],
                    captures_done=row['captures_done'],
                    captures_missed=row['captures_missed'],
                    captures_percent=row['captures_percent'],
                    rakov_cleared=row['rakov_cleared'],
                    tackles_done=row['tackles_done'],
                    meters_covered=row['meters_covered'],
                    defenders_beaten=row['defenders_beaten'],
                    breakthroughs=row['breakthroughs'],
                    attempts_grounded=row['attempts_grounded'],
                    realizations_scored=row['realizations_scored'],
                    realizations_attempted=row['realizations_attempted'],
                    realizations_percent=row['realizations_percent'],
                    penalties_scored=row['penalties_scored'],
                    penalties_attempted=row['penalties_attempted'],
                    penalties_percent=row['penalties_percent'],
                    dropgoals_scored=row['dropgoals_scored'],
                    dropgoals_attempted=row['dropgoals_attempted'],
                    dropgoals_percent=row['dropgoals_percent'],
                    points_scored=row['points_scored'],
                    penalties_received=row['penalties_received'],
                    loss_ball=row['loss_ball'],
                    yellow_cards=row['yellow_cards'],
                    red_cards=row[ 'red_cards'],
                    rating=rating,
                )
                result.append(table_data)

    return result
