from typing import List

from app.models.team_player import TeamPlayer
from app.db_context import sessionmaker
from sqlalchemy import select, insert


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


def get_player_by_api_id(api_id: str):
    with sessionmaker.begin() as session:
        session.expire_on_commit = False
        return (
            session.query(TeamPlayer).where(TeamPlayer.player_api_id == api_id).first()
        )

def insert_one_team_player_db(player: dict):

    with sessionmaker.begin() as session:
        session.expire_on_commit = True
        db_player = TeamPlayer(
            player_api_id=player["player_api_id"],
            full_name=player["full_name"],
            main_position=player["main_position"],
            team_api_id=player["team_api_id"],
            team_id=player["team_id"],
        )
        id = None
        session.add(db_player)
        session.flush()

        session.refresh(db_player)
        id = db_player.id

        session.commit()
        return id
