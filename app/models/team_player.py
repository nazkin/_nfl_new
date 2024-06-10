from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TeamPlayer(Base):
    __tablename__ = "team_player"
    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    player_api_id = Column("player_api_id", String(225))
    full_name = Column("full_name", String(200))
    birth_date = Column("birth_date", String(200))
    weight = Column("weight", Integer())
    height = Column("height", Integer())
    main_position = Column("main_position", String(10))
    birth_place = Column("birth_place", String(220))
    rookie_year = Column("rookie_year", Integer())
    status = Column("status", String(220))
    experience = Column("experience", Integer())
    team_api_id = Column("team_api_id", String(200))
    team_id = Column("team_id", Integer())
