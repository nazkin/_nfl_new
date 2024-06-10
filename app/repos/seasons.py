from typing import List

from app.models.seasons import SeasonsTable, SeasonSchedule
from app.db_context import sessionmaker


def insert_season(seasons: List[SeasonSchedule]):
    with sessionmaker.begin() as session:
        # try:
        seasons_table_data = []
        for season in seasons:
            seasons_table_data.append(
                SeasonsTable(
                    season_api_id=season.season_api_id,
                    year=season.year,
                    season_type=season.season_type,
                    season_status=season.season_status,
                )
            )

        try:
            session.bulk_save_objects(seasons_table_data)
            session.commit()
            session.flush()
        except Exception as ex:
            print(f"Exception storing seasons: {ex}")

        return seasons_table_data
