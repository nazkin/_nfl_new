from typing import List

from app.models.team_player import TeamPlayer
from app.db_context import sessionmaker


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


async def fetch_player_by_api_id(api_id: str):
    with sessionmaker.begin() as session:
        session.expire_on_commit = False
        return (
            session.query(TeamPlayer).where(TeamPlayer.player_api_id == api_id).first()
        )
