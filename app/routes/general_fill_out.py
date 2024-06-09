import requests, time
from fastapi import APIRouter
from typing import List

from app.models.seasons import SeasonSchedule
from app.models.teams_profile import TeamsProfile
from app.models.team_player import TeamPlayer
from app.repos.seasons import insert_season
from app.repos.teams_profile import insert_team_profile
from app.repos.team_players import insert_team_players as repo_insert_team

API_KEY = "QRIw08tTmh5eOtehVHnz59j7V5FUB7L55we4yoTX"
MIN_SEASON_YEAR = 2018

# This router fills out Seasons Table, Teams Table and Players Table
# Nothing Associated with game stats or season stats, just bare minimal
router = APIRouter(prefix="/api/general", tags=["General Tables"])


@router.get("/seasons")
async def fetch_seasons():
    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/league/seasons.json?api_key={API_KEY}"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    return dict(response.json())

# RUN 1: Fill-OUT ALl SEASONS
@router.post("/seasons")
async def post_seasons_to_db():
    data = await fetch_seasons()
    needed_seasons = []
    for season in data["seasons"]:
        if season["year"] > MIN_SEASON_YEAR:
            season_to_model = SeasonSchedule(season_api_id=season["id"], year=season["year"], season_type=season["type"]["code"], season_status=season["status"])
            needed_seasons.append(season_to_model)
    try:
        inserted = insert_season(needed_seasons)
    except Exception as ex:
        print(ex)
    return "Success"

router.get('team_roster/{id}')
async def fetch_team_roster(id: str):
    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/teams/{id}/full_roster.json?api_key={API_KEY}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    team_roster = dict(response.json())
    return team_roster

@router.get('/teams')
async def fetch_all_nfl_teams():
    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/league/teams.json?api_key={API_KEY}"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    teams = dict(response.json())["teams"]

    return len(teams)

@router.post("team_player/{id}")
async def insert_team_players(id: int, inserted_team_api_id: str, players: List):
    # Change players from object to TeamPlayer model
    player_list_to_insert = []
    for player in players:
        print(player)
        player_to_insert = TeamPlayer(
            player_api_id = player["id"],
            full_name = player["name"],
            birth_date = str(player.get('birth_date')),
            weight = player["weight"],
            height = player["height"],
            main_position = player["position"],
            birth_place = player["birth_place"],
            rookie_year = player.get("rookie_year") or None,
            status = player["status"],
            experience = player["experience"],
            team_api_id = inserted_team_api_id,
            team_id = id
        )
        player_list_to_insert.append(player_to_insert)
    
    # Pass the values to repo layer for a bulk insert
    try:
        response = repo_insert_team(player_list_to_insert)
    except Exception as ex:
        print('Could not bulk insert players from team_id {id} or {inserted_team_api_id}: {ex}')
        raise Exception
    
    return response
    
# Run 2: Fill_Out_team_rosters and team_players for each team
@router.post("/team/{id}")
async def fill_out_all_team_rosters(id):
    tp = await fetch_team_roster(id)
    players = tp["players"]

    if id != tp["id"]:
        print('WRONG ID PASSED TO FILL A TEAM')
        return

    # Inserting team  
    teams_profile = TeamsProfile(
        team_api_id=id,
        name = tp["name"],
        alias=tp["alias"],
        market=tp["market"],
        founded=tp["founded"],
        championships_won=tp["championships_won"],
        conference_titles=tp["conference_titles"],
        division_titles=tp["division_titles"],
        playoff_appearances=tp["playoff_appearances"],
        division_name=tp["division"]["name"],
        conference_name=tp["conference"]["name"],
        venue_name=tp["venue"]["name"],
        venue_api_id=tp["venue"]["id"],
        venue_roof_type=tp["venue"]["roof_type"],
        venue_surface=tp["venue"]["surface"],
        venue_city=tp["venue"]["city"],
        venue_state=tp["venue"]["state"]
    )
    try:
        inserted_team_id = await insert_team_profile(teams_profile)
    except Exception as ex:
        print(f"Could not insert team {teams_profile.name}: {ex}")
        raise Exception

    # Inserting players in bulk
    try:
        inserted_teams_players = await insert_team_players(inserted_team_id, id, players=players)
    except Exception as ex:
        print(f"Could not batch insert team members{teams_profile.name}: {ex}")
        raise Exception
    return {
        "team_id": inserted_team_id,
        "InsertedPlayers": inserted_teams_players
    }

