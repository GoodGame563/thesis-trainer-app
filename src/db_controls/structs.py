from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from models import Player, Role, Team


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

    def to_model(self) -> Player:
        return Player(
            id=self.id,
            full_name=self.full_name,
            weight=self.weight,
            height=self.height,
            path_to_photo=self.foto,
            birth_date=date.fromisoformat(self.date_birth),
        )


class Teams(Base):
    __tablename__ = "teams"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    logo: Mapped[str]

    def to_model(self) -> Team:
        return Team(id=self.id, name=self.name, path_to_logo=self.logo)


class Roles(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def to_model(self) -> Role:
        return Role[self.name]


class Games(Base):
    __tablename__ = "games"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    first_team: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    second_team: Mapped[int] = mapped_column(ForeignKey("teams.id"))


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


class Transfers(Base):
    __tablename__ = "transfers"

    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    date: Mapped[str]
