from datetime import date

import aiosqlite
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.orm import aliased

from models import AllStat, Game, Role, ShortTableData, TableData, Team

from .structs import AllStats, Games, Players, Roles, Teams


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


async def get_all_games(async_session: async_sessionmaker[AsyncSession]) -> list[Game]:
    async with async_session() as session:
        team1 = aliased(Teams)
        team2 = aliased(Teams)
        query = (
            select(Games, team1, team2)
            .join(team1, Games.first_team == team1.id)
            .join(team2, Games.second_team == team2.id)
        )
        return [
            Game(g.id, g.name, t1.to_model(), t2.to_model())
            for g, t1, t2 in (await session.execute(query)).tuples()
        ]


async def add_game(
    async_session: async_sessionmaker[AsyncSession], first_team: Team, second_team: Team
):
    async with async_session() as session, session.begin():
        new_game = Games(
            f"{first_team.name} vs {second_team.name}",
            first_team.id,
            second_team.id,
        )
        session.add(new_game)
        await session.flush()
        return new_game.id


async def add_stat(async_session: async_sessionmaker[AsyncSession], stat: AllStat):
    async with async_session() as session, session.begin():
        query = select(Players.id).where(Players.full_name == stat.player_name)
        player_id = (await session.execute(query)).scalar()
        if player_id is None:
            return
        session.add(
            AllStats(
                player_id=player_id,
                team_id=stat.team,
                role_id=Role[stat.role].value,
                game_id=stat.game_id,
                minutes_played=stat.minutes_played,
                successful_passes=stat.successful_passes,
                bad_passes=stat.bad_passes,
                ball_losses=stat.ball_losses,
                carriers=stat.carriers,
                defenders_beaten=stat.defenders_beaten,
                dominant_tackles=stat.dominant_tackles,
                line_break_assists=stat.line_break_assists,
                line_breaks=stat.line_breaks,
                lineout_lose=stat.lineout_lose,
                lineout_steal=stat.lineout_steal,
                lineout_win=stat.lineout_win,
                metres_carried=stat.metres_carried,
                miss_conversions=stat.miss_conversions,
                miss_drop_goal=stat.miss_drop_goal,
                miss_penalties=stat.miss_penalties,
                miss_tackle=stat.miss_tackle,
                penalty=stat.penalty,
                points=stat.points,
                red_card=stat.red_card,
                ruck_cleared=stat.ruck_cleared,
                scrums_lose=stat.scrums_lose,
                scrums_steal=stat.scrums_steal,
                scrums_win=stat.scrums_win,
                steals=stat.steals,
                successful_conversions=stat.successful_conversions,
                successful_drop_goal=stat.successful_drop_goal,
                successful_penalties=stat.successful_penalties,
                successful_tackle=stat.successful_tackle,
                tries=stat.tries,
                try_assists=stat.try_assists,
                yellow_card=stat.yellow_card,
            )
        )
