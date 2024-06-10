from pydantic import BaseModel

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class SeasonSchedule(BaseModel):
    season_api_id: str
    year: int
    season_type: str
    season_status: str


class SeasonsTable(Base):
    __tablename__ = "season_schedule"
    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    season_api_id = Column("season_api_id", String(225))
    year = Column("year", Integer())
    season_type = Column("season_type", String(225))
    season_status = Column("season_status", String(225))
