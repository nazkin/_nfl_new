from typing import List

from app.models.player_season_statistics import PlayerSeasonStats
from app.db_context import sessionmaker


def bulk_insert_all_player_season_stats(stats: List[PlayerSeasonStats]):
    with sessionmaker.begin() as session:

        try:
            session.bulk_save_objects(stats)
            session.commit()
            session.flush()
        except Exception as ex:
            print(f"Exception storing seasons: {ex}")
            raise Exception

        return "Successfully saved all player season stats"
