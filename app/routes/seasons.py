import requests
from fastapi import APIRouter

from app.models.seasons import SeasonSchedule
from app.repos.seasons import insert_season
from app.db_context import API_KEY


MIN_SEASON_YEAR = 2018

router = APIRouter(prefix="/api", tags=["Seasons"])


@router.get("/seasons")
def fetch_seasons():
    # Fetch seasons data from api #
    # Used by post_seasons_to_db  #
    # Return a dict               #
    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/league/seasons.json?api_key={API_KEY}"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    return dict(response.json())


# RUN 1: Mass insert all seasons that are to be used "REG" and "PST"
@router.post("/seasons")
def post_seasons_to_db():
    # Add all available seasons to db            #
    #                                            #
    # Returns "Success" when its successful      #
    data = fetch_seasons()
    needed_seasons = []
    for season in data["seasons"]:
        if season["year"] > MIN_SEASON_YEAR:
            season_to_model = SeasonSchedule(
                season_api_id=season["id"],
                year=season["year"],
                season_type=season["type"]["code"],
                season_status=season["status"],
            )
            needed_seasons.append(season_to_model)
    try:
        inserted = insert_season(needed_seasons)
    except Exception as ex:
        print(ex)
    return "Success"
