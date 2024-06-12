import requests, time
from fastapi import APIRouter
from app.routes.team_and_players_general import (
    fetch_all_nfl_teams_from_db,
    fetch_player_by_api_id,
)
from app.repos.player_season_stats import bulk_insert_all_player_season_stats
from app.models.team_season_statistics import TeamSeasonStats
from app.models.player_season_statistics import TeamPlayerStatsReturn, PlayerSeasonStats
from app.db_context import API_KEY


router = APIRouter(prefix="/api", tags=["PlayerSeasonStats"])


# Fetch Data from API
@router.get("/player_season_stats/{season_year}/{season_type}")
async def fetch_players_season_stats(
    season_year: int, season_type: str
) -> TeamPlayerStatsReturn:
    # Fetch all the NFL teams from the api                         #
    # For each team we create custo, object for the team players  #
    # Return a List[TeamPlayer] and 2 other team identifies       #

    all_teams = await fetch_all_nfl_teams_from_db()
    team_player_stats = []
    for team in all_teams:

        time.sleep(5)
        url = f"https://api.sportradar.com/nfl/official/trial/v7/en/seasons/{season_year}/{season_type}/teams/{team_api_id}/statistics.json?api_key={API_KEY}"

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

    return players_statistic_per_team


# Run 4: Fill out player stats for each team each season
@router.post("/player_season_stats/{season_year}/{season_type}")
async def batch_fill_out_player_season_stats(season_year: int, season_type: str):
    list_of_player_stats_for_batch_store = []
    team_players_stats = await fetch_players_season_stats(season_year, season_type)

    for player in team_players_stats["player_stats"]:
        player_db = await fetch_player_by_api_id(player["id"])

        # Player table model
        p_model = PlayerSeasonStats(
            player_id=player_db.id,
            player_api_id=player["id"],
            team_id=team_players_stats.team_id_db,
            team_api_id=team_players_stats.team_api_id,
            season_year=season_year,
            season_type=season_type,
            games_played=player.get("games_played"),
            games_started=player.get("games_started"),
        )

        if player.get("rushing"):
            p_model.rushing_avg_yards = player["rushing"].get("avg_yards")
            p_model.rushing_attempts = player["rushing"].get("attempts")
            p_model.rushing_touchdowns = player["rushing"].get("touchdowns")
            p_model.rushing_tlost = player["rushing"].get("tlost")
            p_model.rushing_tlost_yards = player["rushing"].get("tlost_yards")
            p_model.rushing_yards = player["rushing"].get("yards")
            p_model.rushing_longest = player["rushing"].get("longest")
            p_model.rushing_longest_touchdown = player["rushing"].get(
                "longest_touchdown"
            )
            p_model.rushing_redzone_attempts = player["rushing"].get("redzone_attempts")
            p_model.rushing_brocken_tackles = player["rushing"].get("broken_tackles")
            p_model.rushing_kneel_downs = player["rushing"].get("kneel_downs")
            p_model.rushing_scrambles = player["rushing"].get("scrambles")
            p_model.rushing_yards_after_contact = player["rushing"].get(
                "yards_after_contact"
            )
        else:
            p_model.rushing_avg_yards = None
            p_model.rushing_attempts = None
            p_model.rushing_touchdowns = None
            p_model.rushing_tlost = None
            p_model.rushing_tlost_yards = None
            p_model.rushing_yards = None
            p_model.rushing_longest = None
            p_model.rushing_longest_touchdown = None
            p_model.rushing_redzone_attempts = None
            p_model.rushing_brocken_tackles = None
            p_model.rushing_kneel_downs = None
            p_model.rushing_scrambles = None
            p_model.rushing_yards_after_contact = None

        if player.get("receiving"):
            p_model.receiving_targets = player["receiving"].get("targets")
            p_model.receiving_receptions = player["receiving"].get("receptions")
            p_model.receiving_avg_yards = player["receiving"].get("avg_yards")
            p_model.receiving_yards = player["receiving"].get("yards")
            p_model.receiving_touchdowns = player["receiving"].get("touchdowns")
            p_model.receiving_yards_after_catch = player["receiving"].get(
                "yards_after_catch"
            )
            p_model.receiving_longest = player["receiving"].get("longest")
            p_model.receiving_longest_touchdown = player["receiving"].get(
                "longest_touchdown"
            )
            p_model.receiving_redzone_targets = player["receiving"].get(
                "redzone_targets"
            )
            p_model.receiving_air_yards = player["receiving"].get("air_yards")
            p_model.receiving_broken_tackles = player["receiving"].get("broken_tackles")
            p_model.receiving_dropped_passes = player["receiving"].get("dropped_passes")
            p_model.receiving_catchable_passes = player["receiving"].get(
                "catchable_passes"
            )
            p_model.receiving_yards_after_contact = player["receiving"].get(
                "yards_after_contact"
            )
        else:
            p_model.receiving_targets = None
            p_model.receiving_receptions = None
            p_model.receiving_avg_yards = None
            p_model.receiving_yards = None
            p_model.receiving_touchdowns = None
            p_model.receiving_yards_after_catch = None
            p_model.receiving_longest = None
            p_model.receiving_longest_touchdown = None
            p_model.receiving_redzone_targets = None
            p_model.receiving_air_yards = (None,)
            p_model.receiving_broken_tackles = None
            p_model.receiving_dropped_passes = None
            p_model.receiving_catchable_passes = None
            p_model.receiving_yards_after_contact = None

        if player.get("penalties"):
            p_model.penalties_penalties = player["penalties"].get("penalties")
            p_model.penalties_yards = player["penalties"].get("yards")
        else:
            p_model.penalties_penalties = None
            p_model.penalties_yards = None

        if player.get("passing"):
            p_model.passing_attempts = player["passing"].get("attempts")
            p_model.passing_completions = player["passing"].get("completions")
            p_model.passing_cmp_pct = player["passing"].get("cmp_pct")
            p_model.passing_interceptions = player["passing"].get("interceptions")
            p_model.passing_sack_yards = player["passing"].get("sack_yards")
            p_model.passing_rating = player["passing"].get("rating")
            p_model.passing_touchdowns = player["passing"].get("touchdowns")
            p_model.passing_avg_yards = player["passing"].get("avg_yards")
            p_model.passing_sacks = player["passing"].get("sacks")
            p_model.passing_longest = player["passing"].get("longest")
            p_model.passing_longest_touchdown = player["passing"].get(
                "longest_touchdown"
            )
            p_model.passing_air_yards = player["passing"].get("air_yards")
            p_model.passing_redzone_attempts = player["passing"].get("redzone_attempts")
            p_model.passing_net_yards = player["passing"].get("net_yards")
            p_model.passing_yards = player["passing"].get("yards")
            p_model.passing_gross_yards = player["passing"].get("gross_yards")
            p_model.passing_int_touchdowns = player["passing"].get("int_touchdowns")
            p_model.passing_throw_aways = player["passing"].get("throw_aways")
            p_model.passing_poor_throws = player["passing"].get("poor_throws")
            p_model.passing_defended_passes = player["passing"].get("defended_passes")
            p_model.passing_dropped_passes = player["passing"].get("dropped_passes")
            p_model.passing_spikes = player["passing"].get("spikes")
            p_model.passing_blitzes = player["passing"].get("blitzes")
            p_model.passing_hurries = player["passing"].get("hurries")
            p_model.passing_knockdowns = player["passing"].get("knockdowns")
            p_model.passing_pocket_time = player["passing"].get("pocket_time")
            p_model.passing_batted_passes = player["passing"].get("batted_passes")
            p_model.passing_on_target_throws = player["passing"].get("on_target_throws")
        else:
            p_model.passing_attempts = None
            p_model.passing_completions = None
            p_model.passing_cmp_pct = None
            p_model.passing_interceptions = None
            p_model.passing_sack_yards = None
            p_model.passing_rating = None
            p_model.passing_touchdowns = None
            p_model.passing_avg_yards = None
            p_model.passing_sacks = None
            p_model.passing_longest = None
            p_model.passing_longest_touchdown = None
            p_model.passing_air_yards = None
            p_model.passing_redzone_attempts = None
            p_model.passing_net_yards = None
            p_model.passing_yards = None
            p_model.passing_gross_yards = None
            p_model.passing_int_touchdowns = None
            p_model.passing_throw_aways = None
            p_model.passing_poor_throws = None
            p_model.passing_defended_passes = None
            p_model.passing_dropped_passes = None
            p_model.passing_spikes = None
            p_model.passing_blitzes = None
            p_model.passing_hurries = None
            p_model.passing_knockdowns = None
            p_model.passing_pocket_time = None
            p_model.passing_batted_passes = None
            p_model.passing_on_target_throws = None

        if player.get("kickoffs"):
            p_model.kickoffs_endzone = player["kickoffs"].get("endzone")
            p_model.kickoffs_inside_20 = player["kickoffs"].get("inside_20")
            p_model.kickoffs_return_yards = player["kickoffs"].get("return_yards")
            p_model.kickoffs_returned = player["kickoffs"].get("returned")
            p_model.kickoffs_touchbacks = player["kickoffs"].get("touchbacks")
            p_model.kickoffs_yards = player["kickoffs"].get("yards")
            p_model.kickoffs_out_of_bounds = player["kickoffs"].get("out_of_bounds")
            p_model.kickoffs_kickoffs = player["kickoffs"].get("kickoffs")
            p_model.kickoffs_onside_successes = player["kickoffs"].get(
                "onside_attempts"
            )
            p_model.kickoffs_onside_attempts = player["kickoffs"].get(
                "onside_successes"
            )
            p_model.kickoffs_squib_kicks = player["kickoffs"].get("squib_kicks")
        else:
            p_model.endzone = None
            p_model.inside_20 = None
            p_model.return_yards = None
            p_model.returned = None
            p_model.touchbacks = None
            p_model.yards = None
            p_model.out_of_bounds = None
            p_model.kickoffs = None
            p_model.onside_successes = None
            p_model.onside_attempts = None
            p_model.squib_kicks = None

        if player.get("kick_returns"):
            p_model.kick_returns_avg_yards = (player["kick_returns"].get("avg_yards"),)
            p_model.kick_returns_yards = (player["kick_returns"].get("yards"),)
            p_model.kick_returns_longest = (player["kick_returns"].get("longest"),)
            p_model.kick_returns_touchdowns = (
                player["kick_returns"].get("touchdowns"),
            )
            p_model.kick_returns_longest_touchdown = (
                player["kick_returns"].get("longest_touchdown"),
            )
            p_model.kick_returns_faircatches = (
                player["kick_returns"].get("faircatches"),
            )
            p_model.kick_returns_returns = (player["kick_returns"].get("returns"),)
        else:
            p_model.returns_avg_yards = None
            p_model.returns_yards = None
            p_model.returns_longest = None
            p_model.returns_touchdowns = None
            p_model.returns_longest_touchdown = None
            p_model.returns_faircatches = None
            p_model.returns_returns = None

        if player.get("int_returns"):
            p_model.int_returns_avg_yards = (player["int_returns"].get("avg_yards"),)
            p_model.int_returns_yards = (player["int_returns"].get("yards"),)
            p_model.int_returns_longest = (player["int_returns"].get("longest"),)
            p_model.int_returns_touchdowns = (player["int_returns"].get("touchdowns"),)
            p_model.int_returns_longest_touchdown = (
                player["int_returns"].get("longest_touchdown"),
            )
            p_model.int_returns_returns = (player["int_returns"].get("returns"),)
        else:
            p_model.int_returns_avg_yards = None
            p_model.int_returns_yards = None
            p_model.int_returns_longest = None
            p_model.int_returns_touchdowns = None
            p_model.int_returns_longest_touchdown = None
            p_model.int_returns_returns = None

        if player.get("fumbles"):
            p_model.fumbles_fumbles = (player["fumbles"].get("fumbles"),)
            p_model.fumbles_lost_fumbles = (player["fumbles"].get("lost_fumbles"),)
            p_model.fumbles_own_rec = (player["fumbles"].get("own_rec"),)
            p_model.fumbles_own_rec_yards = (player["fumbles"].get("own_rec_yards"),)
            p_model.fumbles_opp_rec = (player["fumbles"].get("opp_rec"),)
            p_model.fumbles_out_of_bounds = (player["fumbles"].get("out_of_bounds"),)
            p_model.fumbles_forced_fumbles = (player["fumbles"].get("forced_fumbles"),)
            p_model.fumbles_own_rec_tds = (player["fumbles"].get("own_rec_tds"),)
            p_model.fumbles_opp_rec_tds = (player["fumbles"].get("opp_rec_tds"),)
            p_model.fumbles_ez_rec_tds = (player["fumbles"].get("ez_rec_tds"),)
        else:
            p_model.fumbles_fumbles = None
            p_model.fumbles_lost_fumbles = None
            p_model.fumbles_own_rec = None
            p_model.fumbles_own_rec_yards = None
            p_model.fumbles_opp_rec = None
            p_model.fumbles_out_of_bounds = None
            p_model.fumbles_forced_fumbles = None
            p_model.fumbles_own_rec_tds = None
            p_model.fumbles_opp_rec_tds = None
            p_model.fumbles_ez_rec_tds = None

        if player.get("field_goals"):
            p_model.field_goals_attempts = (player["field_goals"].get("attempts"),)
            p_model.field_goals_made = (player["field_goals"].get("made"),)
            p_model.field_goals_blocked = (player["field_goals"].get("blocked"),)
            p_model.field_goals_yards = (player["field_goals"].get("yards"),)
            p_model.field_goals_avg_yards = (player["field_goals"].get("avg_yards"),)
            p_model.field_goals_longest = (player["field_goals"].get("longest"),)
            p_model.field_goals_missed = (player["field_goals"].get("missed"),)
            p_model.field_goals_pct = (player["field_goals"].get("pct"),)
            p_model.field_goals_attempts_19 = (
                player["field_goals"].get("attempts_19"),
            )
            p_model.field_goals_attempts_29 = (
                player["field_goals"].get("attempts_29"),
            )
            p_model.field_goals_attempts_39 = (
                player["field_goals"].get("attempts_39"),
            )
            p_model.field_goals_attempts_49 = (
                player["field_goals"].get("attempts_49"),
            )
            p_model.field_goals_attempts_50 = (
                player["field_goals"].get("attempts_50"),
            )
            p_model.field_goals_made_19 = (player["field_goals"].get("made_19"),)
            p_model.field_goals_made_29 = (player["field_goals"].get("made_29"),)
            p_model.field_goals_made_39 = (player["field_goals"].get("made_39"),)
            p_model.field_goals_made_49 = (player["field_goals"].get("made_49"),)
            p_model.field_goals_made_50 = (player["field_goals"].get("made_50"),)
        else:
            p_model.field_goals_made = None
            p_model.field_goals_blocked = None
            p_model.field_goals_yards = None
            p_model.field_goals_avg_yards = None
            p_model.field_goals_longest = None
            p_model.field_goals_missed = None
            p_model.field_goals_pct = None
            p_model.field_goals_attempts_19 = None
            p_model.field_goals_attempts_29 = None
            p_model.field_goals_attempts_39 = None
            p_model.field_goals_attempts_49 = None
            p_model.field_goals_attempts_50 = None
            p_model.field_goals_made_19 = None
            p_model.field_goals_made_29 = None
            p_model.field_goals_made_39 = None
            p_model.field_goals_made_49 = None
            p_model.field_goals_made_50 = None

        if player.get("defence"):
            p_model.defence_tackles = (player["defense"].get("tackles"),)
            p_model.defence_assists = (player["defense"].get("assists"),)
            p_model.defence_combined = (player["defense"].get("combined"),)
            p_model.defence_sacks = (player["defense"].get("sacks"),)
            p_model.defence_sack_yards = (player["defense"].get("sack_yards"),)
            p_model.defence_interceptions = (player["defense"].get("interceptions"),)
            p_model.defence_passes_defended = (
                player["defense"].get("passes_defended"),
            )
            p_model.defence_forced_fumbles = (player["defense"].get("forced_fumbles"),)
            p_model.defence_fumble_recoveries = (
                player["defense"].get("fumble_recoveries"),
            )
            p_model.defence_qb_hits = (player["defense"].get("qb_hits"),)
            p_model.defence_tloss = (player["defense"].get("tloss"),)
            p_model.defence_tloss_yards = (player["defense"].get("tloss_yards"),)
            p_model.defence_safeties = (player["defense"].get("safeties"),)
            p_model.defence_sp_tackles = (player["defense"].get("sp_tackles"),)
            p_model.defence_sp_assists = (player["defense"].get("sp_assists"),)
            p_model.defence_sp_forced_fumbles = (
                player["defense"].get("sp_forced_fumbles"),
            )
            p_model.defence_sp_fumble_recoveries = (
                player["defense"].get("sp_fumble_recoveries"),
            )
            p_model.defence_sp_blocks = (player["defense"].get("sp_blocks"),)
            p_model.defence_misc_tackles = (player["defense"].get("misc_tackles"),)
            p_model.defence_misc_assists = (player["defense"].get("misc_assists"),)
            p_model.defence_misc_forced_fumbles = (
                player["defense"].get("misc_forced_fumbles"),
            )
            p_model.defence_misc_fumble_recoveries = (
                player["defense"].get("misc_fumble_recoveries"),
            )
            p_model.defence_def_targets = (player["defense"].get("def_targets"),)
            p_model.defence_def_comps = (player["defense"].get("def_comps"),)
            p_model.defence_blitzes = (player["defense"].get("blitzes"),)
            p_model.defence_hurries = (player["defense"].get("hurries"),)
            p_model.defence_knockdowns = (player["defense"].get("knockdowns"),)
            p_model.defence_missed_tackles = (player["defense"].get("missed_tackles"),)
            p_model.defence_batted_passes = (player["defense"].get("batted_passes"),)
            p_model.defence_three_and_outs_forced = (
                player["defense"].get("three_and_outs_forced"),
            )
            p_model.defence_fourth_down_stops = (
                player["defense"].get("fourth_down_stops"),
            )
        else:
            p_model.defence_tackles = None
            p_model.defence_assists = None
            p_model.defence_combined = None
            p_model.defence_sacks = None
            p_model.defence_sack_yards = None
            p_model.defence_interceptions = None
            p_model.defence_passes_defended = None
            p_model.defence_forced_fumbles = None
            p_model.defence_fumble_recoveries = None
            p_model.defence_qb_hits = None
            p_model.defence_tloss = None
            p_model.defence_tloss_yards = None
            p_model.defence_safeties = None
            p_model.defence_sp_tackles = None
            p_model.defence_sp_assists = None
            p_model.defence_sp_forced_fumbles = None
            p_model.defence_sp_fumble_recoveries = None
            p_model.defence_sp_blocks = None
            p_model.defence_misc_tackles = None
            p_model.defence_misc_assists = None
            p_model.defence_misc_forced_fumbles = None
            p_model.defence_misc_fumble_recoveries = None
            p_model.defence_def_targets = None
            p_model.defence_def_comps = None
            p_model.defence_blitzes = None
            p_model.defence_hurries = None
            p_model.defence_knockdowns = None
            p_model.defence_missed_tackles = None
            p_model.defence_batted_passes = None
            p_model.defence_three_and_outs_forced = None
            p_model.defence_fourth_down_stops = None

        if player.get("extra_points"):
            p_model.extra_points_kicks_attempts = (
                player["extra_points"]["kicks"].get("attempts"),
            )
            p_model.extra_points_kicks_blocked = (
                player["extra_points"]["kicks"].get("blocked"),
            )
            p_model.extra_points_kicks_made = (
                player["extra_points"]["kicks"].get("made"),
            )
            p_model.extra_points_kicks_pct = (
                player["extra_points"]["kicks"].get("pct"),
            )
            p_model.extra_points_conversions_pass_attempts = (
                player["extra_points"]["conversions"].get("pass_attempts"),
            )
            p_model.extra_points_conversions_pass_successes = (
                player["extra_points"]["conversions"].get("pass_successes"),
            )
            p_model.extra_points_conversions_rush_attempts = (
                player["extra_points"]["conversions"].get("rush_attempts"),
            )
            p_model.extra_points_conversions_rush_successes = (
                player["extra_points"]["conversions"].get("rush_successes"),
            )
            p_model.extra_points_conversions_defense_attempts = (
                player["extra_points"]["conversions"].get("defense_attempts"),
            )
            p_model.extra_points_conversions_defense_successes = (
                player["extra_points"]["conversions"].get("defense_successes"),
            )
            p_model.extra_points_conversions_turnover_successes = (
                player["extra_points"]["conversions"].get("turnover_successes"),
            )
        else:
            p_model.extra_points_kicks_attempts = None
            p_model.extra_points_kicks_blocked = None
            p_model.extra_points_kicks_made = None
            p_model.extra_points_kicks_pct = None
            p_model.extra_points_conversions_pass_attempts = None
            p_model.extra_points_conversions_pass_successes = None
            p_model.extra_points_conversions_rush_attempts = None
            p_model.extra_points_conversions_rush_successes = None
            p_model.extra_points_conversions_defense_attempts = None
            p_model.extra_points_conversions_defense_successes = None
            p_model.extra_points_conversions_turnover_successes = None

        if player.get("conversions"):
            p_model.conversions_pass_attempts = player.get("conversions").get(
                "pass_attempts"
            )
            p_model.conversions_pass_successes = player.get("conversions").get(
                "pass_successes"
            )
            p_model.conversions_rush_attempts = player.get("conversions").get(
                "rush_attempts"
            )
            p_model.conversions_rush_successes = player.get("conversions").get(
                "rush_successes"
            )
            p_model.conversions_defense_attempts = player.get("conversions").get(
                "defense_attempts"
            )
            p_model.conversions_defense_successes = player.get("conversions").get(
                "defense_successes"
            )
            p_model.conversions_turnover_successes = player.get("conversions").get(
                "turnover_successes"
            )
        else:
            p_model.conversions_pass_attempts = None
            p_model.conversions_pass_successes = None
            p_model.conversions_rush_attempts = None
            p_model.conversions_rush_successes = None
            p_model.conversions_defense_attempts = None
            p_model.conversions_defense_successes = None
            p_model.conversions_turnover_successes = None

        list_of_player_stats_for_batch_store.append(p_model)

    bulk_store = await bulk_insert_all_player_season_stats(
        list_of_player_stats_for_batch_store
    )

    return bulk_store
