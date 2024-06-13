import requests
from typing import List
from fastapi import APIRouter

from app.models.season_game import SeasonGame
from app.repos.seasons import insert_season
from app.db_context import API_KEY


MIN_SEASON_YEAR = 2018

router = APIRouter(prefix="/api", tags=["games"])


@router.get("/games/{season_year}/{season_type}")
def fetch_seasons() -> List[SeasonGame]:
    # FETCH FROM API #
    # return List[SeasonGame] (all games per season & season type) #
    pass


@router.post("/games/{season_year}/{season_type}")
def batch_insert_seasonal_games() -> str:
    pass
