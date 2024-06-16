import requests, time
from typing import List
from fastapi import APIRouter

from app.repos.player_game_stats import insert_player_game_stats
from app.routes.games import fetch_game_by_api_id, fetch_games_by_seaon_year
from app.routes.team_and_players_general import fetch_player_by_api_id
from app.models.team_game_statistics import TeamGameStats
from app.db_context import API_KEY
from app.routes.utils.utils import (
    organize_player_game_stats,
    generate_playergamestat_model,
)
from app.routes.utils.small_helpers import insert_non_existing_player


MIN_SEASON_YEAR = 2018

router = APIRouter(prefix="/api/player", tags=["game_stats"])


@router.get("/game_stats/{game_api_id}")
def fetch_player_game_stats_api(game_api_id: str):
    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/games/{game_api_id}/statistics.json?api_key={API_KEY}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    data = dict(response.json())

    s_year = data["summary"]["season"]["year"]
    s_type = data["summary"]["season"]["type"]

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


@router.post("/game_stats")
def insert_all_player_game_stats():

    try:
        # ADD GAMES BY YEAR TO SAVE API RESOURCES
        all_games_1 = fetch_games_by_seaon_year(2023)
    except Exception as ex:
        print(f"Could not fetch all games for batch insert")
        raise Exception
    player_game_stats_list = []
    all_games = all_games_1[0:1]
    for game in all_games:

        player_game_stats = fetch_player_game_stats_api(game.game_api_id)
        for player in player_game_stats:
            player_db = fetch_player_by_api_id(player.player_api_id)
            if player_db:
                player.player_id = player_db.id
            else:
                # This means we dont have this player in roster, must insert
                player.player_id = insert_non_existing_player(player)

            player_game_stats_list.append(player)
    for pg_stats in player_game_stats_list:
        value = insert_player_game_stats(pg_stats)
        print(value)

    return "Kaboom"
