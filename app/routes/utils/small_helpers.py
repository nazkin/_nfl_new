from app.repos.team_players import insert_one_team_player_db
from app.models.player_game_statistics import PlayerGameStats
from app.models.player_season_statistics import PlayerSeasonStats
from typing import Union


def insert_non_existing_player(
    player: Union[PlayerGameStats, PlayerSeasonStats],
) -> int:
    player_data = {
        "player_api_id": player.player_api_id,
        "full_name": player.player_name,
        "main_position": player.player_position,
        "jersey": player.player_jersey,
        "team_api_id": player.team_api_id,
        "team_id": player.team_id,
    }
    inserted_player_id = insert_one_team_player_db(player_data)

    return inserted_player_id
