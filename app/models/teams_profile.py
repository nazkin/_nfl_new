

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TeamsProfile(Base):
    __tablename__ = "teams_profile"
    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    team_api_id = Column("team_api_id", String(225))
    name = Column("name", String(200))
    alias = Column("alias", String(200))
    market = Column("market", String(200))
    founded = Column("founded", Integer())
    championships_won = Column("championships_won", Integer())
    conference_titles = Column("conference_titles", Integer())
    division_titles = Column("division_titles", Integer())
    playoff_appearances = Column("playoff_appearances", Integer())
    division_name = Column("division_name", String(200))
    conference_name = Column("conference_name", String(200))
    venue_name = Column("venue_name", String(200))
    venue_api_id = Column("venue_api_id", String(200))
    venue_roof_type = Column("venue_roof_type", String(200))
    venue_surface = Column("venue_surface", String(200))
    venue_city = Column("venue_city", String(200))
    venue_state = Column("venue_state", String(200))
