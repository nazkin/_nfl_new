import requests, time
from fastapi import APIRouter
from app.routes.team_and_players_general import (
    fetch_all_nfl_teams_from_db,
    fetch_player_by_api_id,
)
from app.repos.player_season_stats import bulk_insert_all_player_season_stats
from app.routes.utils.utils import generate_playerseasonstats_model
from app.db_context import API_KEY


router = APIRouter(prefix="/api/player", tags=["PlayerSeasonStats"])


# Fetch Data from API for batch insert
@router.get("/player_season_stats/{season_year}/{season_type}")
def fetch_players_season_stats(season_year: int, season_type: str):
    # Fetch all the NFL player season stats from the api for batch insertion#
    # For each team we create custo, object for the team player stats #
    # Return a List[{team_id_db: int, team_api_id: str, player_stats: List[dict] }]#

    all_teams = fetch_all_nfl_teams_from_db()
    team_player_stats = []

    for team in all_teams:
        print(team.id, team.team_api_id)
        time.sleep(4)
        url = f"https://api.sportradar.com/nfl/official/trial/v7/en/seasons/{season_year}/{season_type}/teams/{team.team_api_id}/statistics.json?api_key={API_KEY}"

        headers = {"accept": "application/json"}

        response = requests.get(url, headers=headers)
        team_stats = dict(response.json())

        if season_type == "PST" and not team_stats.get("record"):
            print(f"Team {team.name} did not make it to playoffs during {season_year}")
            continue

        players_statistic_per_team = {
            "team_id_db": team.id,
            "team_api_id": team.team_api_id,
            "player_stats": team_stats["players"],
        }

        team_player_stats.append(players_statistic_per_team)

    return team_player_stats


# Run 4: Fill out player stats for each team each season
@router.post("/player_season_stats/{season_year}/{season_type}")
def batch_fill_out_player_season_stats(season_year: int, season_type: str):
    # Use "/player_season_stats/{season_year}/{season_type}" to get all player stats for each team #
    # Stats are fetched per season and season type "REG" or "PST" #
    # Returns a success string from repo layer if everything works #

    list_of_player_stats_for_batch_store = []
    team_players_stats = fetch_players_season_stats(season_year, season_type)

    for stats in team_players_stats:
        for player in stats["player_stats"]:
            # Fetch player from team_player table so that we can find FK id
            player_db = fetch_player_by_api_id(player["id"])

            # Generate the table model necessary for insert
            p_model = generate_playerseasonstats_model(
                player, stats, player_db, season_year, season_type
            )
            list_of_player_stats_for_batch_store.append(p_model)

    bulk_store = bulk_insert_all_player_season_stats(
        list_of_player_stats_for_batch_store
    )

    return bulk_store
