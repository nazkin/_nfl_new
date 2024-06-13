from typing import List

from app.models.team_season_statistics import TeamSeasonStats
from app.db_context import sessionmaker


def bulk_insert_all_teams_season_stats(stats: List[TeamSeasonStats]):
    with sessionmaker.begin() as session:

        try:
            session.bulk_save_objects(stats)
            session.commit()
            session.flush()
        except Exception as ex:
            print(f"Exception storing seasons: {ex}")
            raise Exception

        return "Successfully save team season stats"
