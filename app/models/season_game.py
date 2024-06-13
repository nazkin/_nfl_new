from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SeasonGame(Base):
    __tablename__ = "season_game"

    id = Column(Integer, primary_key=True)
    game_api_id = Column(String(225), unique=True, nullable=False)
    status = Column(String(225))
    scheduled = Column(String(225))
    game_type = Column(String(225))
    is_conference_game = Column(Boolean)
    duration = Column(String(10))
    venue_name = Column(String(225))
    venue_api_id = Column(String(225))
    venue_city = Column(String(225))
    venue_lat = Column(String(225))
    venue_long = Column(String(225))
    home_team_name = Column(String(200))
    home_team_alias = Column(String(10))
    home_team_api_id = Column(String(200))
    home_team_game_number = Column(Integer)
    away_team_name = Column(String(200))
    away_team_alias = Column(String(10))
    away_team_api_id = Column(String(200))
    away_team_game_number = Column(Integer)
    humidity = Column(Integer)
    temperature = Column(Integer)
    wind_direction = Column(String(5))
    wind_speed = Column(Integer)
    total_home_points = Column(Integer)
    total_away_points = Column(Integer)
    q1_home_points = Column(Integer)
    q1_away_points = Column(Integer)
    q2_home_points = Column(Integer)
    q2_away_points = Column(Integer)
    q3_home_points = Column(Integer)
    q3_away_points = Column(Integer)
    q4_home_points = Column(Integer)
    q4_away_points = Column(Integer)