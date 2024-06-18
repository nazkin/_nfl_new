import requests, time
from fastapi import APIRouter
from app.routes.team_and_players_general import fetch_all_nfl_teams_from_db
from app.models.team_season_statistics import TeamSeasonStats
from app.repos.team_season_stats import bulk_insert_all_teams_season_stats
from app.utils.utils import generate_teamseasonstats_model
from app.db_context import API_KEY


router = APIRouter(prefix="/api/team", tags=["TeamSeasonStats"])

# Fetch Data from API
@router.get("/season_stats/{season_year}/{season_type}")
def fetch_team_season_stats(season_year: int, season_type: str):
    # Fetch all the NFL teams from the api                                          #
    # For each team we create TeamSeasonStats object for the team and its oponents  #
    # Return a List[TeamSeasonStats] to bulk insert it in a different route         #

    all_teams = fetch_all_nfl_teams_from_db()
    team_stats_final = []
    for team in all_teams:
        team_id_db = team.id
        team_api_id = team.team_api_id
        time.sleep(5)
        url = f"https://api.sportradar.com/nfl/official/trial/v7/en/seasons/{season_year}/{season_type}/teams/{team_api_id}/statistics.json?api_key={API_KEY}"

        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers)
        team_stats = dict(response.json())
        team_stats["db_team_id"] = team_id_db
        team_stats["team_api_id"] = team_api_id
        # Team Stats for the season
        ts = team_stats.get("record")
        team_season_stats_for = generate_teamseasonstats_model(team_id_db, team_api_id, season_year, season_type, ts, True)
        if not ts:
            print(
                f"Team {team.name} did not make it to playoffs during {season_year} or has no stats for this {season_type} season"
            )
            continue
        # season stats for the team against opponents


        # season stats of opponents against team
        os = team_stats["opponents"]
        team_stats_opponent = generate_teamseasonstats_model(team_id_db, team_api_id, season_year, season_type, ts, False)
        team_stats_final.append(team_season_stats_for)
        team_stats_final.append(team_stats_opponent)
    return team_stats_final


# Run 3: Fill out team statistics per season and season type
@router.post("/season_stats/{season_year}/{season_type}")
def batch_insert_season_team_statistics(season_year: int, season_type: str):
    # Batch insert the List[TeamSeasonStats] for a specific season type and year    #
    #                                                                               #
    # Return a success string to signify successful entry                           #

    all_teams_season_stats = []
    try:
        all_teams_season_stats = fetch_team_season_stats(season_year, season_type)
    except Exception as ex:
        print(
            f"Could not fetch season stats for teams of {season_year}-{season_type}: {ex}"
        )
        raise Exception
    try:
        insert_value = bulk_insert_all_teams_season_stats(all_teams_season_stats)
    except Exception as ex:
        print(
            f"Could not fetch season stats for teams of {season_year}-{season_type}: {ex}"
        )
        raise Exception

    return insert_value
