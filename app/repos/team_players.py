from typing import List

from app.models.team_player import TeamPlayer
from app.db_context import sessionmaker
from sqlalchemy import select


def insert_team_players(team_players: List[TeamPlayer]):
    with sessionmaker.begin() as session:

        try:
            session.bulk_save_objects(team_players)
            session.commit()
            session.flush()
        except Exception as ex:
            print(f"Exception storing seasons: {ex}")
            raise Exception

        return "success"


async def get_player_by_api_id(api_id: str):
    value: TeamPlayer = None
    with sessionmaker.begin() as session:
        session.expire_on_commit = False
        stmt = select(TeamPlayer).where(TeamPlayer.player_api_id == api_id)

        value = session.execute(stmt)
    return value
