import requests, time
from typing import List
from fastapi import APIRouter

from app.models.season_game import SeasonGame
from app.repos.games import (
    bulk_insert_season_games,
    get_game_by_api_id,
    get_all_games_from_db,
    get_all_games_by_season_year,
)
from app.repos.games import update_game_weather
from app.routes.team_and_players_general import fetch_team_by_api_id
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


@router.get("/api_seasonal/{season_year}/{season_type}")
def fetch_games_from_api(season_year: int, season_type: str):
    # FETCH FROM API #
    # return List[dicts]  #

    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/games/{season_year}/{season_type}/schedule.json?api_key={API_KEY}"

    headers = {"accept": "application/json"}

    data = requests.get(url, headers=headers)
    games_data = dict(data.json())["weeks"]

    return games_data


@router.get("/fetch_and_convert/{season_year}/{season_type}")
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

            game_for_db = SeasonGame(
                game_api_id=game["id"],
                season_year=season_year,
                season_type=season_type,
                status=game["status"],
                scheduled=game["scheduled"],
                is_conference_game=game.get("conference_game"),
                duration=game.get("duration"),
                venue_name=game["venue"]["name"],
                venue_api_id=game["venue"]["id"],
                venue_city=game["venue"]["city"],
                home_team_id=home_team_db.id,
                home_team_name=game["home"]["name"],
                home_team_alias=game["home"]["alias"],
                home_team_api_id=game["home"]["id"],
                home_team_game_number=game["home"].get("game_number"),
                away_team_id=awat_team_db.id,
                away_team_name=game["away"]["name"],
                away_team_alias=game["away"]["alias"],
                away_team_api_id=game["away"]["id"],
                away_team_game_number=game["away"].get("game_number"),
                total_home_points=game["scoring"]["home_points"],
                total_away_points=game["scoring"]["away_points"],
            )
            # some years dont specify this so we can generate it
            if game.get("game_type"):
                game_for_db.game_type = game.get("game_type")
            else:
                if season_type == "REG":
                    game_for_db.game_type = "regular"

                if season_type == "PST":
                    game_for_db.game_type = "playoff"

            # this was created as part of a game_id that has no statistics no score etc (can be removed now)
            if game.get("venue").get("location"):
                game_for_db.venue_lat = (game["venue"].get("location")["lat"],)
                game_for_db.venue_long = (game["venue"].get("location")["lng"],)
            else:
                game_for_db.venue_lat = None
                game_for_db.venue_long = None
            # this was created as part of a game_id that has no statistics no score etc (can be removed now)
            if game.get("weather"):
                if game.get("weather").get("condition"):
                    game_for_db.weather_condition = game["weather"].get("condition")

                if game.get("weather").get("humidity"):
                    game_for_db.humidity = game["weather"]["humidity"]

                if game.get("weather").get("temp"):
                    game_for_db.temperature = game["weather"]["temp"]

                if game.get("weather").get("wind"):
                    game_for_db.wind_direction = game["weather"]["wind"].get(
                        "direction"
                    )
                    game_for_db.wind_speed = game["weather"]["wind"].get("speed")

            for period in game["scoring"]["periods"]:
                if period["number"] == 1:
                    game_for_db.q1_home_points = period["home_points"]
                    game_for_db.q1_away_points = period["away_points"]
                elif period["number"] == 2:
                    game_for_db.q2_home_points = period["home_points"]
                    game_for_db.q2_away_points = period["away_points"]
                elif period["number"] == 3:
                    game_for_db.q3_home_points = period["home_points"]
                    game_for_db.q3_away_points = period["away_points"]
                elif period["number"] == 4:
                    game_for_db.q4_home_points = period["home_points"]
                    game_for_db.q4_away_points = period["away_points"]
                else:
                    print(
                        f"ERROR: Game period outside of 4 shouldnt exist for game {game['id']}"
                    )
            games_list.append(game_for_db)

    return games_list


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
