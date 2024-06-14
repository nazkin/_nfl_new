from typing import List

from app.models.season_game import SeasonGame
from app.db_context import sessionmaker


def bulk_insert_season_games(games: List[SeasonGame]):
    with sessionmaker.begin() as session:

        try:
            session.bulk_save_objects(games)
            session.commit()
            session.flush()
        except Exception as ex:
            print(f"Exception storing seasons: {ex}")
            raise Exception

        return "Successfully saved all season games"


def get_game_by_api_id(api_id: str):
    with sessionmaker.begin() as session:
        session.expire_on_commit = False
        return session.query(SeasonGame).where(SeasonGame.game_api_id == api_id).first()


def get_all_games_from_db():
    with sessionmaker.begin() as session:
        session.expire_on_commit = False
        return session.query(SeasonGame).where(SeasonGame.id > 0).all()


def get_all_games_by_season_year(year: int):
    with sessionmaker.begin() as session:
        session.expire_on_commit = False
        values = session.query(SeasonGame).where(SeasonGame.season_year == year).all()
        return values
