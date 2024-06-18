import requests, time
from fastapi import APIRouter

from app.utils.utils import (
    organize_player_game_stats,
    generate_playergamestat_model,
)
from app.utils.small_helpers import insert_non_existing_player
from app.routes.games import fetch_game_by_api_id, fetch_games_by_seaon_year
from app.routes.team_and_players_general import fetch_player_by_api_id
from app.db_context import API_KEY
from app.repos.player_game_stats import insert_player_game_stats


router = APIRouter(prefix="/api/player", tags=["player_game_stats"])


@router.get("/game_stats/{game_api_id}")
def fetch_player_game_stats_api(game_api_id: str):
    # Fetch all player stats per game from an api
    # Args: game_api_id -> game identifier in api
    # Returns: List[PlayerGameStats] for home and away team combined

    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/games/{game_api_id}/statistics.json?api_key={API_KEY}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    data = dict(response.json())

    s_year = data["summary"]["season"]["year"]
    s_type = data["summary"]["season"]["type"]

    if not data.get("statistics"):
        print(f"could not find any game_statistics for game number {game_api_id}")
        return []

    # data fetched from db needed for home and away teams models

    general_game_db = fetch_game_by_api_id(game_api_id)
    home_stats = organize_player_game_stats(
        data["statistics"]["home"], game_api_id, general_game_db, True, s_year, s_type
    )
    away_stats = organize_player_game_stats(
        data["statistics"]["away"], game_api_id, general_game_db, False, s_year, s_type
    )
    all_games_stats_db = [
        *generate_playergamestat_model(home_stats),
        *generate_playergamestat_model(away_stats),
    ]
    return all_games_stats_db

# Run7 - Fill out all player game stats per season
@router.post("/game_stats/{season_year}")
def insert_all_player_game_stats_per_season_year(season_year: int):
    # Insert all player game stats for a particular year
    # Args: Season year
    # Returns { type: "Success string", inserted_ids: List[int]}
    try:
        # ADD GAMES BY YEAR TO SAVE API RESOURCES
        # Year will include REG and PST seasons from database
        all_games = fetch_games_by_seaon_year(season_year)
    except Exception as ex:
        print(f"Could not fetch all games for batch insert")
        raise Exception
    player_game_stats_list = []

    for game in all_games:
        time.sleep(4)
        player_game_stats = fetch_player_game_stats_api(game.game_api_id)
        for player in player_game_stats:
            player_db = fetch_player_by_api_id(player.player_api_id)
            if player_db:
                player.player_id = player_db.id
            else:
                # This means we dont have this player in roster, must insert
                player.player_id = insert_non_existing_player(player)

            player_game_stats_list.append(player)

    inserted_ids = []
    for pg_stats in player_game_stats_list:
        inserted_data = insert_player_game_stats(pg_stats)
        inserted_ids.append(inserted_data)

    return {"type": "Success", "inserted_ids": inserted_ids}
