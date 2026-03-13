from datetime import date

import aiosqlite
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from models import TableData, ShortTableData

from .structs import AllStats, Players, Roles, Teams


async def get_games_statistics(
    async_session: async_sessionmaker[AsyncSession], game_id: int
) -> list[TableData]:
    result = []
    async with async_session() as session:
        stmt = (
            select(AllStats, Players, Teams, Roles)
            .where(AllStats.game_id == game_id)
            .join(Players)
            .join(Teams)
            .join(Roles)
        )
        data = await session.execute(stmt)
        for s, p, t, r in data.tuples():
            player = p.to_model()
            result.append(
                TableData(
                    player=player,
                    role=r.to_model(),
                    date_birth=player.birth_date,
                    team=t.name,
                    minutes_played=s.minutes_played,
                    successful_passes=s.successful_passes,
                    bad_passes=s.bad_passes,
                    successful_tackle=s.successful_tackle,
                    dominant_tackles=s.dominant_tackles,
                    miss_tackle=s.miss_tackle,
                    ruck_cleared=s.ruck_cleared,
                    steals=s.steals,
                    metres_carried=s.metres_carried,
                    defenders_beaten=s.defenders_beaten,
                    carriers=s.carriers,
                    line_breaks=s.line_breaks,
                    line_break_assists=s.line_break_assists,
                    tries=s.tries,
                    try_assists=s.try_assists,
                    successful_conversions=s.successful_conversions,
                    miss_conversions=s.miss_conversions,
                    successful_penalties=s.successful_penalties,
                    miss_penalties=s.miss_penalties,
                    successful_drop_goal=s.successful_drop_goal,
                    miss_drop_goal=s.miss_drop_goal,
                    points=s.points,
                    scrums_win=s.scrums_win,
                    scrums_steal=s.scrums_steal,
                    scrums_lose=s.scrums_lose,
                    lineout_win=s.lineout_win,
                    lineout_steal=s.lineout_steal,
                    lineout_lose=s.lineout_lose,
                    ball_losses=s.ball_losses,
                    penalty=s.penalty,
                    yellow_card=s.yellow_card,
                    red_card=s.red_card,
                    rating=0.0,
                )
            )
    return result


async def get_all_games_by_player_team_id(
    async_session: async_sessionmaker[AsyncSession], player_id: int, team_id: int
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
    async with async_session() as session:
        stmt = (
            select(AllStats, Roles)
            .where(AllStats.player_id == player_id and AllStats.team_id == team_id)
            .join(Roles)
        )
        data = await session.execute(stmt)
        for s, r in data.tuples():
            table_data = ShortTableData(
                role=r.to_model(),
                minutes_played=s.minutes_played,
                successful_passes=s.successful_passes,
                bad_passes=s.bad_passes,
                successful_tackle=s.successful_tackle,
                dominant_tackles=s.dominant_tackles,
                miss_tackle=s.miss_tackle,
                ruck_cleared=s.ruck_cleared,
                steals=s.steals,
                metres_carried=s.metres_carried,
                defenders_beaten=s.defenders_beaten,
                carriers=s.carriers,
                line_breaks=s.line_breaks,
                line_break_assists=s.line_break_assists,
                tries=s.tries,
                try_assists=s.try_assists,
                successful_conversions=s.successful_conversions,
                miss_conversions=s.miss_conversions,
                successful_penalties=s.successful_penalties,
                miss_penalties=s.miss_penalties,
                successful_drop_goal=s.successful_drop_goal,
                miss_drop_goal=s.miss_drop_goal,
                points=s.points,
                scrums_win=s.scrums_win,
                scrums_steal=s.scrums_steal,
                scrums_lose=s.scrums_lose,
                lineout_win=s.lineout_win,
                lineout_steal=s.lineout_steal,
                lineout_lose=s.lineout_lose,
                ball_losses=s.ball_losses,
                penalty=s.penalty,
                yellow_card=s.yellow_card,
                red_card=s.red_card,
                rating=0.0,
            )
            result.append(table_data)

    return result
