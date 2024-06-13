import requests, time
from fastapi import APIRouter
from typing import List


from app.models.teams_profile import TeamsProfile
from app.models.team_player import TeamPlayer
from app.repos.teams_profile import (
    insert_team_profile,
    fetch_all_teams,
    fetch_team_from_db_by_api_id,
)
from app.repos.team_players import (
    insert_team_players as repo_insert_team,
    get_player_by_api_id,
)
from app.db_context import API_KEY


router = APIRouter(prefix="/api", tags=["Team and Players General"])


router.get("/team_roster/{id}")


def fetch_team_roster(id: str):
    # Fetch team roster from API                            #
    #                                                       #
    # Return a dictionary                                   #
    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/teams/{id}/full_roster.json?api_key={API_KEY}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    team_roster = dict(response.json())
    return team_roster


@router.get("/teams")
def fetch_all_nfl_teams():
    # Fetch all nfl teams from API                          #
    #                                                       #
    # Return a dictionary                                   #
    url = f"https://api.sportradar.com/nfl/official/trial/v7/en/league/teams.json?api_key={API_KEY}"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    teams = dict(response.json()["teams"])

    return teams


@router.get("/teams_from_db")
def fetch_all_nfl_teams_from_db():
    # Fetch all nfl teams from DB                           #
    #                                                       #
    # Return a List[TeamsProfile] needed to fetch PK        #

    all_teams = fetch_all_teams()
    return all_teams


@router.get("/teams_from_db/{api_id}")
def fetch_team_by_api_id(api_id):
    # Fetch all nfl teams from DB                           #
    #                                                       #
    # Return a List[TeamsProfile] needed to fetch PK        #

    team = fetch_team_from_db_by_api_id(api_id)
    return team


@router.get("/team_player/{api_id}")
def fetch_player_by_api_id(api_id: str):
    player = get_player_by_api_id(api_id)
    return player


@router.post("/team_player/{id}")
def insert_team_players(id: int, inserted_team_api_id: str, players: List):
    # Inser team Players into db                         #
    # Used by fill_out_all_team_rosters                   #
    # Return a List[TeamsProfile] needed to fetch PK        #
    player_list_to_insert = []
    for player in players:
        player_to_insert = TeamPlayer(
            player_api_id=player["id"],
            full_name=player["name"],
            birth_date=str(player.get("birth_date")),
            weight=player.get("weight"),
            height=player.get("height"),
            main_position=player.get("main_position"),
            birth_place=player.get("birth_place"),
            rookie_year=player.get("rookie_year") or None,
            status=player.get("status"),
            experience=player.get("experience"),
            team_api_id=inserted_team_api_id,
            team_id=id,
        )
        player_list_to_insert.append(player_to_insert)

    # Pass the values to repo layer for a bulk insert
    try:
        response = repo_insert_team(player_list_to_insert)
    except Exception as ex:
        print(
            "Could not bulk insert players from team_id {id} or {inserted_team_api_id}: {ex}"
        )
        raise Exception

    return response


# Run 2: Fill_Out_team_rosters and team_players for each team
@router.post("/team/{id}")
def fill_out_all_team_rosters(id):
    # Fill out general teams and rosters of teams          #
    #  Process: Plug in each team id into post URL 1 by 1  #
    # Returns a custom dict signifying stuff was inserted   #
    tp = fetch_team_roster(id)
    players = tp["players"]

    if id != tp["id"]:
        print("WRONG ID PASSED TO FILL A TEAM")
        return

    # Inserting team
    teams_profile = TeamsProfile(
        team_api_id=id,
        name=tp["name"],
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
        venue_state=tp["venue"]["state"],
    )
    try:
        inserted_team_id = insert_team_profile(teams_profile)
    except Exception as ex:
        print(f"Could not insert team {teams_profile.name}: {ex}")
        raise Exception

    # Inserting players in bulk
    try:
        inserted_teams_players = insert_team_players(
            inserted_team_id, id, players=players
        )
    except Exception as ex:
        print(f"Could not batch insert team members{teams_profile.name}: {ex}")
        raise Exception
    return {"team_id": inserted_team_id, "InsertedPlayers": inserted_teams_players}
