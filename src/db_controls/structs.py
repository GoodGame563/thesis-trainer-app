from datetime import date as DATE

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from models import Player, Role, Team, Transfer


class Base(DeclarativeBase):
    pass


class Players(Base):
    __tablename__ = "players"
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]
    height: Mapped[float]
    weight: Mapped[float]
    date_birth: Mapped[str]
    foto: Mapped[str]

    def __init__(
        self, full_name: str, height: float, weight: float, date_birth: DATE, foto: str
    ):
        self.full_name = full_name
        self.date_birth = date_birth.isoformat()
        self.foto = foto
        self.height = height
        self.weight = weight

    def to_model(self) -> Player:
        return Player(
            id=self.id,
            full_name=self.full_name,
            weight=self.weight,
            height=self.height,
            path_to_photo=self.foto,
            birth_date=DATE.fromisoformat(self.date_birth),
        )


class Teams(Base):
    __tablename__ = "teams"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    logo: Mapped[str]

    def __init__(self, name: str, path_to_logo: str):
        self.name = name
        self.logo = path_to_logo

    def to_model(self) -> Team:
        return Team(id=self.id, name=self.name, path_to_logo=self.logo)


class Roles(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def __init__(self, name: str):
        self.name = name

    def to_model(self) -> Role:
        return Role[self.name]


class Games(Base):
    __tablename__ = "games"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    first_team: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    second_team: Mapped[int] = mapped_column(ForeignKey("teams.id"))

    def __init__(self, name: str, first_team: int, second_team: int):
        self.name = name
        self.first_team = first_team
        self.second_team = second_team


class AllStats(Base):
    __tablename__ = "all_stats"

    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"))

    minutes_played: Mapped[int]

    # ============= ПЕРЕДАЧИ =============
    successful_passes: Mapped[int]
    bad_passes: Mapped[int]

    # ============= ЗАХВАТЫ =============
    successful_tackle: Mapped[int]
    dominant_tackles: Mapped[int]
    miss_tackle: Mapped[int]

    # ============= РАКИ И ОТБОРЫ =============
    ruck_cleared: Mapped[int]
    steals: Mapped[int]

    # ============= ПРОНОС И ОБЫГРЫВАНИЕ =============
    metres_carried: Mapped[int]
    defenders_beaten: Mapped[int]
    carriers: Mapped[int]

    # ============= ПРОРЫВЫ =============
    line_breaks: Mapped[int]
    line_break_assists: Mapped[int]

    # ============= ПОПЫТКИ И АССИСТЫ =============
    tries: Mapped[int]
    try_assists: Mapped[int]

    # ============= УДАРЫ: УСПЕШНЫЕ =============
    successful_conversions: Mapped[int]
    successful_penalties: Mapped[int]
    successful_drop_goal: Mapped[int]

    # ============= УДАРЫ: НЕУДАЧНЫЕ =============
    miss_conversions: Mapped[int]
    miss_penalties: Mapped[int]
    miss_drop_goal: Mapped[int]

    # ============= ОЧКИ =============
    points: Mapped[int]

    # ============= СХВАТКИ =============
    scrums_win: Mapped[int]
    scrums_steal: Mapped[int]
    scrums_lose: Mapped[int]

    # ============= КОРИДОРЫ (ЛИНЕЙ-АУТЫ) =============
    lineout_win: Mapped[int]
    lineout_steal: Mapped[int]
    lineout_lose: Mapped[int]

    # ============= НАРУШЕНИЯ И ПОТЕРИ =============
    ball_losses: Mapped[int]
    penalty: Mapped[int]

    # ============= КАРТОЧКИ =============
    yellow_card: Mapped[int]
    red_card: Mapped[int]

    def __init__(
        self,
        player_id: int,
        team_id: int,
        role_id: int,
        game_id: int,
        minutes_played: int = 0,
        successful_passes: int = 0,
        bad_passes: int = 0,
        successful_tackle: int = 0,
        dominant_tackles: int = 0,
        miss_tackle: int = 0,
        ruck_cleared: int = 0,
        steals: int = 0,
        metres_carried: int = 0,
        defenders_beaten: int = 0,
        carriers: int = 0,
        line_breaks: int = 0,
        line_break_assists: int = 0,
        tries: int = 0,
        try_assists: int = 0,
        successful_conversions: int = 0,
        successful_penalties: int = 0,
        successful_drop_goal: int = 0,
        miss_conversions: int = 0,
        miss_penalties: int = 0,
        miss_drop_goal: int = 0,
        points: int = 0,
        scrums_win: int = 0,
        scrums_steal: int = 0,
        scrums_lose: int = 0,
        lineout_win: int = 0,
        lineout_steal: int = 0,
        lineout_lose: int = 0,
        ball_losses: int = 0,
        penalty: int = 0,
        yellow_card: int = 0,
        red_card: int = 0,
    ):
        self.player_id = player_id
        self.team_id = team_id
        self.role_id = role_id
        self.game_id = game_id
        self.minutes_played = minutes_played
        self.successful_passes = successful_passes
        self.bad_passes = bad_passes
        self.successful_tackle = successful_tackle
        self.dominant_tackles = dominant_tackles
        self.miss_tackle = miss_tackle
        self.ruck_cleared = ruck_cleared
        self.steals = steals
        self.metres_carried = metres_carried
        self.defenders_beaten = defenders_beaten
        self.carriers = carriers
        self.line_breaks = line_breaks
        self.line_break_assists = line_break_assists
        self.tries = tries
        self.try_assists = try_assists
        self.successful_conversions = successful_conversions
        self.successful_penalties = successful_penalties
        self.successful_drop_goal = successful_drop_goal
        self.miss_conversions = miss_conversions
        self.miss_penalties = miss_penalties
        self.miss_drop_goal = miss_drop_goal
        self.points = points
        self.scrums_win = scrums_win
        self.scrums_steal = scrums_steal
        self.scrums_lose = scrums_lose
        self.lineout_win = lineout_win
        self.lineout_steal = lineout_steal
        self.lineout_lose = lineout_lose
        self.ball_losses = ball_losses
        self.penalty = penalty
        self.yellow_card = yellow_card
        self.red_card = red_card


class Transfers(Base):
    __tablename__ = "transfers"

    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    date: Mapped[str]

    def __init__(self, player_id: int, team_id: int, transfer_date: DATE):
        self.player_id = player_id
        self.team_id = team_id
        self.date = transfer_date.isoformat()
