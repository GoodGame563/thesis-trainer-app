from datetime import date

from models import Player, Role, TableData, Team

from .db_connection import db_connect


def get_games_statistics() -> list[TableData]:
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

    conn = db_connect()
    cur = conn.cursor()

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
    """

    cur.execute(query)
    rows = cur.fetchall()
    conn.close()

    result = []
    for row in rows:
        birth_date = date.fromisoformat(row[3]) if row[3] else date.today()

        team = Team(name=row[5], path_to_logo=row[6])

        player = Player(
            nst=row[0],
            weight=row[1],
            height=row[2],
            team=team,
            birth_date=birth_date,
            path_to_photo=row[4],
        )

        role = ROLE_MAPPING.get(row[7], Role.NOTHING)

        rating = 0.0

        table_data = TableData(
            player=player,
            role=role,
            minutes_played=row[8],
            passes_accurate=row[9],
            passes_inaccurate=row[10],
            passes_percent=row[11],
            captures_done=row[12],
            captures_missed=row[13],
            captures_percent=row[14],
            rakov_cleared=row[15],
            tackles_done=row[16],
            meters_covered=row[17],
            defenders_beaten=row[18],
            breakthroughs=row[19],
            attempts_grounded=row[20],
            realizations_scored=row[21],
            realizations_attempted=row[22],
            realizations_percent=row[23],
            penalties_scored=row[24],
            penalties_attempted=row[25],
            penalties_percent=row[26],
            dropgoals_scored=row[27],
            dropgoals_attempted=row[28],
            dropgoals_percent=row[29],
            points_scored=row[30],
            penalties_received=row[31],
            loss_ball=row[32],
            yellow_cards=row[33],
            red_cards=row[34],
            rating=rating,
        )
        result.append(table_data)

    return result
