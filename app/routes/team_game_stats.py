import requests, time
from typing import List
from fastapi import APIRouter

from app.models.team_game_statistics import TeamGameStats
from app.repos.team_game_stats import batch_insert_team_game_stats
from app.routes.games import fetch_game_by_api_id, fetch_games_by_seaon_year
from app.db_context import API_KEY
from app.routes.utils.utils import generate_teamgamestat_model


MIN_SEASON_YEAR = 2018

router = APIRouter(prefix="/api", tags=["game_stats"])


@router.get("/game_stats/{game_api_id}")
def fetch_team_game_stats_api(game_api_id: str):
    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/games/{game_api_id}/statistics.json?api_key={API_KEY}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    data = dict(response.json())
    # data fetched from db needed for home and away teams models
    general_game_db = fetch_game_by_api_id(game_api_id)
    home_stats = data["statistics"]["home"]
    away_stats = data["statistics"]["away"]
    season_year = data["summary"]["season"]["year"]
    season_type = data["summary"]["season"]["type"]

    home_stats_model = generate_teamgamestat_model(
        general_game_db, home_stats, season_year, season_type, isHome=True
    )

    away_stats_model = generate_teamgamestat_model(
        general_game_db, away_stats, season_year, season_type, isHome=False
    )

    return {"home_stats": home_stats_model, "away_stats": away_stats_model}


@router.post("/game_stats/")
def insert_all_team_game_stats():

    try:
        all_games = fetch_games_by_seaon_year(2023)
    except Exception as ex:
        print(f"Could not fetch all games for batch insert")
        raise Exception
    team_game_stats_list = []

    for game in all_games:
        time.sleep(4)
        team_game_stats = fetch_team_game_stats_api(game.game_api_id)
        team_game_stats_list.append(team_game_stats["home_stats"])
        team_game_stats_list.append(team_game_stats["away_stats"])

    return batch_insert_team_game_stats(team_game_stats)
