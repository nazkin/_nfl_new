from app.models.player_game_statistics import PlayerGameStats
from app.db_context import sessionmaker


def insert_player_game_stats(stats: PlayerGameStats):
    # inserts PlayerGameStats object one-by-one
    # Args: PlayerGameStats object
    # Return: id, the PK of the player_game_stats database
    with sessionmaker.begin() as session:
        session.expire_on_commit = True
        id = None
        session.add(stats)
        session.flush()

        session.refresh(stats)
        id = stats.id
        session.commit()
        return id
