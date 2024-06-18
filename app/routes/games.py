import requests
from typing import List
from fastapi import APIRouter

from app.repos.games import (
    bulk_insert_season_games,
    get_game_by_api_id,
    get_all_games_from_db,
    get_all_games_by_season_year,
)
from app.repos.games import update_game_weather
from app.routes.team_and_players_general import fetch_team_by_api_id
from app.utils.utils import generate_seasongame_model
from app.db_context import API_KEY


router = APIRouter(prefix="/api/games", tags=["games"])


@router.get("/fetch_all_db")
def fetch_all_games_from_db():
    return get_all_games_from_db()


@router.get("/fetch_one_db/{api_id}")
def fetch_game_by_api_id(api_id: str):
    return get_game_by_api_id(api_id)


@router.get("/fetch_all_db/{season_year}")
def fetch_games_by_seaon_year(season_year: int):
    games = get_all_games_by_season_year(season_year)
    return games


@router.get("/fetch_all_api/{season_year}/{season_type}")
def fetch_games_from_api(season_year: int, season_type: str):
    # FETCH FROM API #
    # return List[dicts]  #

    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/games/{season_year}/{season_type}/schedule.json?api_key={API_KEY}"

    headers = {"accept": "application/json"}

    data = requests.get(url, headers=headers)
    games_data = dict(data.json())["weeks"]

    return games_data


@router.get("/fetch_all_and_convert/{season_year}/{season_type}")
def fetch_games_from_api_and_convert(season_year: int, season_type: str):
    # FETCH FROM API #
    # return List[SeasonGame] (all games per season & season type) #
    games_list = []
    games_data = fetch_games_from_api(season_year, season_type)
    for game_week in games_data:
        for game in game_week["games"]:
            home_team_db = fetch_team_by_api_id(game["home"]["id"])
            awat_team_db = fetch_team_by_api_id(game["away"]["id"])
            if not game.get("scoring"):
                print(f"GAME {game['id']} does not have scores thus is skipped")
                continue

            game_for_db = generate_seasongame_model(game, season_year, season_type, home_team_db.id, awat_team_db.id)
            games_list.append(game_for_db)

    return games_list

#Run 5: Fill out all games for each season and season type
@router.post("/insert_all/{season_year}/{season_type}")
def batch_insert_seasonal_games(season_year: int, season_type: str):
    try:
        games_list = fetch_games_from_api_and_convert(season_year, season_type)
    except Exception as ex:
        print(
            f"Could not fetch games list for nfl season {season_year} {season_type} {ex}"
        )
        raise ex

    try:
        res = bulk_insert_season_games(games_list)
    except Exception as ex:
        print(
            f"Could not bulk insert games list for nfl season {season_year} {season_type} {ex}"
        )
        raise ex

    return res


@router.put("/bulk_update_template/{season_year}/{season_type}")
def update_games_data(season_year: int, season_type: str):
    games_week = fetch_games_from_api(season_year, season_type)
    weeks = []
    weather_list = []
    for week in games_week:
        weeks.append(week)
        for game in week["games"]:

            weather_data = {
                "game_api_id": game["id"],
                "temperature": None,
                "humidity": None,
                "wind_speed": None,
                "wind_direction": None,
            }
            weather = game.get("weather")
            if weather:
                weather_data["humidity"] = weather.get("humidity")
                weather_data["temperature"] = weather.get("temp")
                wind = weather.get("wind")
                if wind:
                    weather_data["wind_speed"] = wind.get("speed")
                    weather_data["wind_direction"] = wind.get("direction")

            weather_list.append(weather_data)
    for weather in weather_list:
        res = update_game_weather(weather)
        print(res)
    return "Successfully updated a bunch of weather for games"
