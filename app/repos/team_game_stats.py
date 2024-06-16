from typing import List

from app.models.team_game_statistics import TeamGameStats
from app.db_context import sessionmaker


def batch_insert_team_game_stats(stats: List[TeamGameStats]):
    with sessionmaker.begin() as session:

        try:
            session.bulk_save_objects(stats)
            session.commit()
            session.flush()
        except Exception as ex:
            print(f"Exception storing team game stats: {ex}")
            raise Exception

        return "Successfully saved team stats for all games"
