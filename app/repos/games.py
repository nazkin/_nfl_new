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
