from app.models.player_game_statistics import PlayerGameStats
from app.db_context import sessionmaker

# ON Conflict unique_key_index
# DO UPDATE SET (col = value)

# In sqlalchemy its
# stmt = insert(model).on_conflict_do_update()
def insert_player_game_stats(stats: PlayerGameStats):
    with sessionmaker.begin() as session:

        try:
            session.add(stats)
            session.flush()
            session.commit()
        except Exception as ex:
            print(f"Exception inserting player game stats: {ex}")
            raise Exception

        return "Successfully saved all player season stats"
