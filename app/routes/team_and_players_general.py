import requests, time
from fastapi import APIRouter
from typing import List

from app.models.teams_profile import TeamsProfile
from app.models.team_player import TeamPlayer, IncompletePlayerBody
from app.repos.teams_profile import (
    insert_team_profile,
    fetch_all_teams,
    fetch_team_from_db_by_api_id,
)
from app.repos.team_players import (
    insert_team_players as repo_insert_team,
    get_player_by_api_id,
    insert_one_team_player_db,
)
from app.db_context import API_KEY


router = APIRouter(prefix="/api/team_and_player", tags=["Team and Players General"])


@router.get("/team_roster/{id}")
def fetch_team_roster_api(id: str):
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
def insert_team_players(id: int, team_api_id: str, players: List):
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
            main_position=player.get("position"),
            birth_place=player.get("birth_place"),
            rookie_year=player.get("rookie_year") or None,
            status=player.get("status"),
            experience=player.get("experience"),
            team_api_id=team_api_id,
            team_id=id,
        )
        if player.get("draft"):
            player_to_insert.draft_year = player.get("draft").get("year")
            player_to_insert.draft_round = player.get("draft").get("round")
            player_to_insert.draft_number = player.get("draft").get("round")

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
@router.post("/teams/{team_api_id}")
def fill_out_a_team_roster(team_api_id, db_team_id=None):
    # Fill out general teams and rosters of teams          #
    #  Process: Plug in each team id into post URL 1 by 1  #
    # Returns a custom dict signifying stuff was inserted   #
    tp = fetch_team_roster_api(team_api_id)
    players = tp["players"]

    if team_api_id != tp["id"]:
        print("WRONG ID PASSED TO FILL A TEAM")
        return

    if not db_team_id:
        db_team = fetch_team_by_api_id(team_api_id)
        db_team_id = db_team.id

    # Inserting team (Uncomment if you want to reinsert teams and rosters from scratch together)
    # teams_profile = generate_teamprofile_model(tp, team_api_id)
    # try:
    #     inserted_team_id = insert_team_profile(teams_profile)
    # except Exception as ex:
    #     print(f"Could not insert team {teams_profile.name}: {ex}")
    #     raise Exception

    # Inserting players in bulk

    try:
        inserted_team_players = insert_team_players(
            db_team_id, team_api_id, players=players
        )
    except Exception as ex:
        print(f"Could not batch insert team members for team_id {db_team_id}: {ex}")
        raise Exception
    return {"team_id": db_team_id, "inserted_players": inserted_team_players}


@router.post("/fill_out_all_teams_rosters")
def fill_out_all_teams_rosters():
    all_teams = fetch_all_nfl_teams_from_db()
    for team in all_teams:
        time.sleep(4)
        response = fill_out_a_team_roster(team.team_api_id, team.id)
        print(response)
    return "Successfully filled all team rosters"


# Insert team player one by one
@router.post("/team_player")
def insert_one_team_player(player: IncompletePlayerBody):
    player_dict = player.model_dump(
        mode="python", exclude_unset=True, exclude_none=True
    )
    try:
        value = insert_one_team_player_db(player_dict)
    except Exception as ex:
        raise ex
    return value
