import requests, time
from fastapi import APIRouter
from app.routes.team_and_players_general import fetch_all_nfl_teams_from_db
from app.models.team_season_statistics import TeamSeasonStats
from app.repos.team_season_stats import bulk_insert_all_teams_season_stats

from app.routes.seasons import API_KEY


router = APIRouter(prefix="/api", tags=["TeamSeasonStats"])

# Fetch Data from API
@router.get("/team_season_stats/{season_year}/{season_type}")
async def fetch_team_season_stats(season_year: int, season_type: str):
    # Fetch all the NFL teams from the api                                          #
    # For each team we create TeamSeasonStats object for the team and its oponents  #
    # Return a List[TeamSeasonStats] to bulk insert it in a different route         #

    all_teams = await fetch_all_nfl_teams_from_db()
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
        # Team Stats
        ts = team_stats["record"]
        team_stats_for = TeamSeasonStats(
            team_id=team_id_db,
            team_api_id=team_api_id,
            season_type=season_type,
            season_year=season_year,
            isoponentstats=False,
            games_played=ts.get("games_played"),
            touchdown_passes=ts["touchdowns"].get("pass"),
            touchdown_rushes=ts["touchdowns"].get("rush"),
            touchdown_total_return=ts["touchdowns"].get("total_return"),
            touchdown_total=ts["touchdowns"].get("total"),
            touchdown_fumble_return=ts["touchdowns"].get("fumble_return"),
            touchdown_int_return=ts["touchdowns"].get("int_return"),
            touchdown_kick_return=ts["touchdowns"].get("kick_return"),
            touchdown_point_return=ts["touchdowns"].get("punt_return"),
            touchdown_other=ts["touchdowns"].get("other"),
            rushing_avg_yards=ts["rushing"].get("avg_yards"),
            rushing_attempts=ts["rushing"].get("attempts"),
            rushing_touchdowns=ts["rushing"].get("touchdowns"),
            rushing_tlost=ts["rushing"].get("tlost"),
            rushing_tlost_yards=ts["rushing"].get("tlost_yards"),
            rushing_yards=ts["rushing"].get("yards"),
            rushing_longest=ts["rushing"].get("longest"),
            rushing_longest_touchdown=ts["rushing"].get("longest_touchdown"),
            rushing_redzone_attempts=ts["rushing"].get("redzone_attempts"),
            rushing_brocken_tackles=ts["rushing"].get("broken_tackles"),
            rushing_kneel_downs=ts["rushing"].get("kneel_downs"),
            rushing_scrambles=ts["rushing"].get("scrambles"),
            rushing_yards_after_contact=ts["rushing"].get("yards_after_contact"),
            receiving_targets=ts["receiving"].get("targets"),
            receiving_receptions=ts["receiving"].get("receptions"),
            receiving_avg_yards=ts["receiving"].get("avg_yards"),
            receiving_yards=ts["receiving"].get("yards"),
            receiving_touchdowns=ts["receiving"].get("touchdowns"),
            receiving_yards_after_catch=ts["receiving"].get("yards_after_catch"),
            receiving_longest=ts["receiving"].get("longest"),
            receiving_longest_touchdown=ts["receiving"].get("longest_touchdown"),
            receiving_redzone_targets=ts["receiving"].get("redzone_targets"),
            receiving_air_yards=ts["receiving"].get("air_yards"),
            receiving_broken_tackles=ts["receiving"].get("broken_tackles"),
            receiving_dropped_passes=ts["receiving"].get("dropped_passes"),
            receiving_catchable_passes=ts["receiving"].get("catchable_passes"),
            receiving_yards_after_contact=ts["receiving"].get("yards_after_contact"),
            punts_attempts=ts["punts"].get("attempts"),
            punts_yards=ts["punts"].get("yards"),
            punts_net_yards=ts["punts"].get("net_yards"),
            punts_blocked=ts["punts"].get("blocked"),
            punts_touchbacks=ts["punts"].get("touchbacks"),
            punts_inside_20=ts["punts"].get("inside_20"),
            punts_return_yards=ts["punts"].get("return_yards"),
            punts_avg_net_yards=ts["punts"].get("avg_net_yards"),
            punts_avg_yards=ts["punts"].get("avg_yards"),
            punts_longest=ts["punts"].get("longest"),
            punts_hang_time=ts["punts"].get("hang_time"),
            punts_avg_hang_time=ts["punts"].get("avg_hang_time"),
            punt_returns_avg_yards=ts["punt_returns"].get("avg_yards"),
            punt_returns_yards=ts["punt_returns"].get("yards"),
            punt_returns_longest=ts["punt_returns"].get("longest"),
            punt_returns_touchdowns=ts["punt_returns"].get("touchdowns"),
            punt_returns_longest_touchdown=ts["punt_returns"].get("longest_touchdown"),
            punt_returns_faircatches=ts["punt_returns"].get("faircatches"),
            penalties_penalties=ts["penalties"].get("penalties"),
            penalties_yards=ts["penalties"].get("yards"),
            passing_attempts=ts["passing"].get("attempts"),
            passing_completions=ts["passing"].get("completions"),
            passing_cmp_pct=ts["passing"].get("cmp_pct"),
            passing_interceptions=ts["passing"].get("interceptions"),
            passing_sack_yards=ts["passing"].get("sack_yards"),
            passing_rating=ts["passing"].get("rating"),
            passing_touchdowns=ts["passing"].get("touchdowns"),
            passing_avg_yards=ts["passing"].get("avg_yards"),
            passing_sacks=ts["passing"].get("sacks"),
            passing_longest=ts["passing"].get("longest"),
            passing_longest_touchdown=ts["passing"].get("longest_touchdown"),
            passing_air_yards=ts["passing"].get("air_yards"),
            passing_redzone_attempts=ts["passing"].get("redzone_attempts"),
            passing_net_yards=ts["passing"].get("net_yards"),
            passing_yards=ts["passing"].get("yards"),
            passing_gross_yards=ts["passing"].get("gross_yards"),
            passing_int_touchdowns=ts["passing"].get("int_touchdowns"),
            passing_throw_aways=ts["passing"].get("throw_aways"),
            passing_poor_throws=ts["passing"].get("poor_throws"),
            passing_defended_passes=ts["passing"].get("defended_passes"),
            passing_dropped_passes=ts["passing"].get("dropped_passes"),
            passing_spikes=ts["passing"].get("spikes"),
            passing_blitzes=ts["passing"].get("blitzes"),
            passing_hurries=ts["passing"].get("hurries"),
            passing_knockdowns=ts["passing"].get("knockdowns"),
            passing_pocket_time=ts["passing"].get("pocket_time"),
            passing_batted_passes=ts["passing"].get("batted_passes"),
            passing_on_target_throws=ts["passing"].get("on_target_throws"),
            kickoffs_endzone=ts["kickoffs"].get("endzone"),
            kickoffs_inside_20=ts["kickoffs"].get("inside_20"),
            kickoffs_return_yards=ts["kickoffs"].get("return_yards"),
            kickoffs_returned=ts["kickoffs"].get("returned"),
            kickoffs_touchbacks=ts["kickoffs"].get("touchbacks"),
            kickoffs_yards=ts["kickoffs"].get("yards"),
            kickoffs_out_of_bounds=ts["kickoffs"].get("out_of_bounds"),
            kickoffs_kickoffs=ts["kickoffs"].get("kickoffs"),
            kickoffs_onside_successes=ts["kickoffs"].get("onside_attempts"),
            kickoffs_onside_attempts=ts["kickoffs"].get("onside_successes"),
            kickoffs_squib_kicks=ts["kickoffs"].get("squib_kicks"),
            kick_returns_avg_yards=ts["kick_returns"].get("avg_yards"),
            kick_returns_yards=ts["kick_returns"].get("yards"),
            kick_returns_longest=ts["kick_returns"].get("longest"),
            kick_returns_touchdowns=ts["kick_returns"].get("touchdowns"),
            kick_returns_longest_touchdown=ts["kick_returns"].get("longest_touchdown"),
            kick_returns_faircatches=ts["kick_returns"].get("faircatches"),
            kick_returns_returns=ts["kick_returns"].get("returns"),
            interceptions_return_yards=ts["interceptions"].get("return_yards"),
            interceptions_returned=ts["interceptions"].get("returned"),
            interceptions_interceptions=ts["interceptions"].get("interceptions"),
            int_returns_avg_yards=ts["int_returns"].get("avg_yards"),
            int_returns_yards=ts["int_returns"].get("yards"),
            int_returns_longest=ts["int_returns"].get("longest"),
            int_returns_touchdowns=ts["int_returns"].get("touchdowns"),
            int_returns_longest_touchdown=ts["int_returns"].get("longest_touchdown"),
            int_returns_returns=ts["int_returns"].get("returns"),
            fumbles_fumbles=ts["fumbles"].get("fumbles"),
            fumbles_lost_fumbles=ts["fumbles"].get("lost_fumbles"),
            fumbles_own_rec=ts["fumbles"].get("own_rec"),
            fumbles_own_rec_yards=ts["fumbles"].get("own_rec_yards"),
            fumbles_opp_rec=ts["fumbles"].get("opp_rec"),
            fumbles_out_of_bounds=ts["fumbles"].get("out_of_bounds"),
            fumbles_forced_fumbles=ts["fumbles"].get("forced_fumbles"),
            fumbles_own_rec_tds=ts["fumbles"].get("own_rec_tds"),
            fumbles_opp_rec_tds=ts["fumbles"].get("opp_rec_tds"),
            fumbles_ez_rec_tds=ts["fumbles"].get("ez_rec_tds"),
            first_downs_pass=ts["first_downs"].get("pass"),
            first_downs_penalty=ts["first_downs"].get("penalty"),
            first_downs_rush=ts["first_downs"].get("rush"),
            first_downs_total=ts["first_downs"].get("total"),
            field_goals_attempts=ts["field_goals"].get("attempts"),
            field_goals_made=ts["field_goals"].get("made"),
            field_goals_blocked=ts["field_goals"].get("blocked"),
            field_goals_yards=ts["field_goals"].get("yards"),
            field_goals_avg_yards=ts["field_goals"].get("avg_yards"),
            field_goals_longest=ts["field_goals"].get("longest"),
            field_goals_missed=ts["field_goals"].get("missed"),
            field_goals_pct=ts["field_goals"].get("pct"),
            field_goals_attempts_19=ts["field_goals"].get("attempts_19"),
            field_goals_attempts_29=ts["field_goals"].get("attempts_29"),
            field_goals_attempts_39=ts["field_goals"].get("attempts_39"),
            field_goals_attempts_49=ts["field_goals"].get("attempts_49"),
            field_goals_attempts_50=ts["field_goals"].get("attempts_50"),
            field_goals_made_19=ts["field_goals"].get("made_19"),
            field_goals_made_29=ts["field_goals"].get("made_29"),
            field_goals_made_39=ts["field_goals"].get("made_39"),
            field_goals_made_49=ts["field_goals"].get("made_49"),
            field_goals_made_50=ts["field_goals"].get("made_50"),
            defence_tackles=ts["defense"].get("tackles"),
            defence_assists=ts["defense"].get("assists"),
            defence_combined=ts["defense"].get("combined"),
            defence_sacks=ts["defense"].get("sacks"),
            defence_sack_yards=ts["defense"].get("sack_yards"),
            defence_interceptions=ts["defense"].get("interceptions"),
            defence_passes_defended=ts["defense"].get("passes_defended"),
            defence_forced_fumbles=ts["defense"].get("forced_fumbles"),
            defence_fumble_recoveries=ts["defense"].get("fumble_recoveries"),
            defence_qb_hits=ts["defense"].get("qb_hits"),
            defence_tloss=ts["defense"].get("tloss"),
            defence_tloss_yards=ts["defense"].get("tloss_yards"),
            defence_safeties=ts["defense"].get("safeties"),
            defence_sp_tackles=ts["defense"].get("sp_tackles"),
            defence_sp_assists=ts["defense"].get("sp_assists"),
            defence_sp_forced_fumbles=ts["defense"].get("sp_forced_fumbles"),
            defence_sp_fumble_recoveries=ts["defense"].get("sp_fumble_recoveries"),
            defence_sp_blocks=ts["defense"].get("sp_blocks"),
            defence_misc_tackles=ts["defense"].get("misc_tackles"),
            defence_misc_assists=ts["defense"].get("misc_assists"),
            defence_misc_forced_fumbles=ts["defense"].get("misc_forced_fumbles"),
            defence_misc_fumble_recoveries=ts["defense"].get("misc_fumble_recoveries"),
            defence_def_targets=ts["defense"].get("def_targets"),
            defence_def_comps=ts["defense"].get("def_comps"),
            defence_blitzes=ts["defense"].get("blitzes"),
            defence_hurries=ts["defense"].get("hurries"),
            defence_knockdowns=ts["defense"].get("knockdowns"),
            defence_missed_tackles=ts["defense"].get("missed_tackles"),
            defence_batted_passes=ts["defense"].get("batted_passes"),
            defence_three_and_outs_forced=ts["defense"].get("three_and_outs_forced"),
            defence_fourth_down_stops=ts["defense"].get("fourth_down_stops"),
            extra_points_kicks_attempts=ts["extra_points"]["kicks"].get("attempts"),
            extra_points_kicks_blocked=ts["extra_points"]["kicks"].get("blocked"),
            extra_points_kicks_made=ts["extra_points"]["kicks"].get("made"),
            extra_points_kicks_pct=ts["extra_points"]["kicks"].get("pct"),
            extra_points_conversions_pass_attempts=ts["extra_points"][
                "conversions"
            ].get("pass_attempts"),
            extra_points_conversions_pass_successes=ts["extra_points"][
                "conversions"
            ].get("pass_successes"),
            extra_points_conversions_rush_attempts=ts["extra_points"][
                "conversions"
            ].get("rush_attempts"),
            extra_points_conversions_rush_successes=ts["extra_points"][
                "conversions"
            ].get("rush_successes"),
            extra_points_conversions_defense_attempts=ts["extra_points"][
                "conversions"
            ].get("defense_attempts"),
            extra_points_conversions_defense_successes=ts["extra_points"][
                "conversions"
            ].get("defense_successes"),
            extra_points_conversions_turnover_successes=ts["extra_points"][
                "conversions"
            ].get("turnover_successes"),
            efficiency_goaltogo_attempts=ts["efficiency"]["goaltogo"].get("attempts"),
            efficiency_goaltogo_successes=ts["efficiency"]["goaltogo"].get("successes"),
            efficiency_goaltogo_pct=ts["efficiency"]["goaltogo"].get("pct"),
            efficiency_redzone_attempts=ts["efficiency"]["redzone"].get("attempts"),
            efficiency_redzone_successes=ts["efficiency"]["redzone"].get("successes"),
            efficiency_redzone_pct=ts["efficiency"]["redzone"].get("pct"),
            efficiency_thirddown_attempts=ts["efficiency"]["thirddown"].get("attempts"),
            efficiency_thirddown_successes=ts["efficiency"]["thirddown"].get(
                "successes"
            ),
            efficiency_thirddown_pct=ts["efficiency"]["thirddown"].get("pct"),
            efficiency_fourthdown_attempts=ts["efficiency"]["fourthdown"].get(
                "attempts"
            ),
            efficiency_fourthdown_successes=ts["efficiency"]["fourthdown"].get(
                "successes"
            ),
            efficiency_fourthdown_pct=ts["efficiency"]["fourthdown"].get("pct"),
        )
        # Oponent Stats
        os = team_stats["opponents"]
        team_stats_opponent = TeamSeasonStats(
            team_id=team_id_db,
            team_api_id=team_api_id,
            season_type=season_type,
            season_year=season_year,
            isoponentstats=True,
            games_played=os.get("games_played"),
            touchdown_passes=os["touchdowns"].get("pass"),
            touchdown_rushes=os["touchdowns"].get("rush"),
            touchdown_total_return=os["touchdowns"].get("total_return"),
            touchdown_total=os["touchdowns"].get("total"),
            touchdown_fumble_return=os["touchdowns"].get("fumble_return"),
            touchdown_int_return=os["touchdowns"].get("int_return"),
            touchdown_kick_return=os["touchdowns"].get("kick_return"),
            touchdown_point_return=os["touchdowns"].get("punt_return"),
            touchdown_other=os["touchdowns"].get("other"),
            rushing_avg_yards=os["rushing"].get("avg_yards"),
            rushing_attempts=os["rushing"].get("attempts"),
            rushing_touchdowns=os["rushing"].get("touchdowns"),
            rushing_tlost=os["rushing"].get("tlost"),
            rushing_tlost_yards=os["rushing"].get("tlost_yards"),
            rushing_yards=os["rushing"].get("yards"),
            rushing_longest=os["rushing"].get("longest"),
            rushing_longest_touchdown=os["rushing"].get("longest_touchdown"),
            rushing_redzone_attempts=os["rushing"].get("redzone_attempts"),
            rushing_brocken_tackles=os["rushing"].get("broken_tackles"),
            rushing_kneel_downs=os["rushing"].get("kneel_downs"),
            rushing_scrambles=os["rushing"].get("scrambles"),
            rushing_yards_after_contact=os["rushing"].get("yards_after_contact"),
            receiving_targets=os["receiving"].get("targets"),
            receiving_receptions=os["receiving"].get("receptions"),
            receiving_avg_yards=os["receiving"].get("avg_yards"),
            receiving_yards=os["receiving"].get("yards"),
            receiving_touchdowns=os["receiving"].get("touchdowns"),
            receiving_yards_after_catch=os["receiving"].get("yards_after_catch"),
            receiving_longest=os["receiving"].get("longest"),
            receiving_longest_touchdown=os["receiving"].get("longest_touchdown"),
            receiving_redzone_targets=os["receiving"].get("redzone_targets"),
            receiving_air_yards=os["receiving"].get("air_yards"),
            receiving_broken_tackles=os["receiving"].get("broken_tackles"),
            receiving_dropped_passes=os["receiving"].get("dropped_passes"),
            receiving_catchable_passes=os["receiving"].get("catchable_passes"),
            receiving_yards_after_contact=os["receiving"].get("yards_after_contact"),
            punts_attempts=os["punts"].get("attempts"),
            punts_yards=os["punts"].get("yards"),
            punts_net_yards=os["punts"].get("net_yards"),
            punts_blocked=os["punts"].get("blocked"),
            punts_touchbacks=os["punts"].get("touchbacks"),
            punts_inside_20=os["punts"].get("inside_20"),
            punts_return_yards=os["punts"].get("return_yards"),
            punts_avg_net_yards=os["punts"].get("avg_net_yards"),
            punts_avg_yards=os["punts"].get("avg_yards"),
            punts_longest=os["punts"].get("longest"),
            punts_hang_time=os["punts"].get("hang_time"),
            punts_avg_hang_time=os["punts"].get("avg_hang_time"),
            punt_returns_avg_yards=os["punt_returns"].get("avg_yards"),
            punt_returns_yards=os["punt_returns"].get("yards"),
            punt_returns_longest=os["punt_returns"].get("longest"),
            punt_returns_touchdowns=os["punt_returns"].get("touchdowns"),
            punt_returns_longest_touchdown=os["punt_returns"].get("longest_touchdown"),
            punt_returns_faircatches=os["punt_returns"].get("faircatches"),
            penalties_penalties=os["penalties"].get("penalties"),
            penalties_yards=os["penalties"].get("yards"),
            passing_attempts=os["passing"].get("attempts"),
            passing_completions=os["passing"].get("completions"),
            passing_cmp_pct=os["passing"].get("cmp_pct"),
            passing_interceptions=os["passing"].get("interceptions"),
            passing_sack_yards=os["passing"].get("sack_yards"),
            passing_rating=os["passing"].get("rating"),
            passing_touchdowns=os["passing"].get("touchdowns"),
            passing_avg_yards=os["passing"].get("avg_yards"),
            passing_sacks=os["passing"].get("sacks"),
            passing_longest=os["passing"].get("longest"),
            passing_longest_touchdown=os["passing"].get("longest_touchdown"),
            passing_air_yards=os["passing"].get("air_yards"),
            passing_redzone_attempts=os["passing"].get("redzone_attempts"),
            passing_net_yards=os["passing"].get("net_yards"),
            passing_yards=os["passing"].get("yards"),
            passing_gross_yards=os["passing"].get("gross_yards"),
            passing_int_touchdowns=os["passing"].get("int_touchdowns"),
            passing_throw_aways=os["passing"].get("throw_aways"),
            passing_poor_throws=os["passing"].get("poor_throws"),
            passing_defended_passes=os["passing"].get("defended_passes"),
            passing_dropped_passes=os["passing"].get("dropped_passes"),
            passing_spikes=os["passing"].get("spikes"),
            passing_blitzes=os["passing"].get("blitzes"),
            passing_hurries=os["passing"].get("hurries"),
            passing_knockdowns=os["passing"].get("knockdowns"),
            passing_pocket_time=os["passing"].get("pocket_time"),
            passing_batted_passes=os["passing"].get("batted_passes"),
            passing_on_target_throws=os["passing"].get("on_target_throws"),
            kickoffs_endzone=os["kickoffs"].get("endzone"),
            kickoffs_inside_20=os["kickoffs"].get("inside_20"),
            kickoffs_return_yards=os["kickoffs"].get("return_yards"),
            kickoffs_returned=os["kickoffs"].get("returned"),
            kickoffs_touchbacks=os["kickoffs"].get("touchbacks"),
            kickoffs_yards=os["kickoffs"].get("yards"),
            kickoffs_out_of_bounds=os["kickoffs"].get("out_of_bounds"),
            kickoffs_kickoffs=os["kickoffs"].get("kickoffs"),
            kickoffs_onside_successes=os["kickoffs"].get("onside_successes"),
            kickoffs_onside_attempts=os["kickoffs"].get("onside_attempts"),
            kickoffs_squib_kicks=os["kickoffs"].get("squib_kicks"),
            kick_returns_avg_yards=os["kick_returns"].get("avg_yards"),
            kick_returns_yards=os["kick_returns"].get("yards"),
            kick_returns_longest=os["kick_returns"].get("longest"),
            kick_returns_touchdowns=os["kick_returns"].get("touchdowns"),
            kick_returns_longest_touchdown=os["kick_returns"].get("longest_touchdown"),
            kick_returns_faircatches=os["kick_returns"].get("faircatches"),
            kick_returns_returns=os["kick_returns"].get("returns"),
            interceptions_return_yards=os["interceptions"].get("return_yards"),
            interceptions_returned=os["interceptions"].get("returned"),
            interceptions_interceptions=os["interceptions"].get("interceptions"),
            int_returns_avg_yards=os["int_returns"].get("avg_yards"),
            int_returns_yards=os["int_returns"].get("yards"),
            int_returns_longest=os["int_returns"].get("longest"),
            int_returns_touchdowns=os["int_returns"].get("touchdowns"),
            int_returns_longest_touchdown=os["int_returns"].get("longest_touchdown"),
            int_returns_returns=os["int_returns"].get("returns"),
            fumbles_fumbles=os["fumbles"].get("fumbles"),
            fumbles_lost_fumbles=os["fumbles"].get("lost_fumbles"),
            fumbles_own_rec=os["fumbles"].get("own_rec"),
            fumbles_own_rec_yards=os["fumbles"].get("own_rec_yards"),
            fumbles_opp_rec=os["fumbles"].get("opp_rec"),
            fumbles_out_of_bounds=os["fumbles"].get("out_of_bounds"),
            fumbles_forced_fumbles=os["fumbles"].get("forced_fumbles"),
            fumbles_own_rec_tds=os["fumbles"].get("own_rec_tds"),
            fumbles_opp_rec_tds=os["fumbles"].get("opp_rec_tds"),
            fumbles_ez_rec_tds=os["fumbles"].get("ez_rec_tds"),
            first_downs_pass=os["first_downs"].get("pass"),
            first_downs_penalty=os["first_downs"].get("penalty"),
            first_downs_rush=os["first_downs"].get("rush"),
            first_downs_total=os["first_downs"].get("total"),
            field_goals_attempts=os["field_goals"].get("attempts"),
            field_goals_made=os["field_goals"].get("made"),
            field_goals_blocked=os["field_goals"].get("blocked"),
            field_goals_yards=os["field_goals"].get("yards"),
            field_goals_avg_yards=os["field_goals"].get("avg_yards"),
            field_goals_longest=os["field_goals"].get("longest"),
            field_goals_missed=os["field_goals"].get("missed"),
            field_goals_pct=os["field_goals"].get("pct"),
            field_goals_attempts_19=os["field_goals"].get("attempts_19"),
            field_goals_attempts_29=os["field_goals"].get("attempts_29"),
            field_goals_attempts_39=os["field_goals"].get("attempts_39"),
            field_goals_attempts_49=os["field_goals"].get("attempts_49"),
            field_goals_attempts_50=os["field_goals"].get("attempts_50"),
            field_goals_made_19=os["field_goals"].get("made_19"),
            field_goals_made_29=os["field_goals"].get("made_29"),
            field_goals_made_39=os["field_goals"].get("made_39"),
            field_goals_made_49=os["field_goals"].get("made_49"),
            field_goals_made_50=os["field_goals"].get("made_50"),
            defence_tackles=os["defense"].get("tackles"),
            defence_assists=os["defense"].get("assists"),
            defence_combined=os["defense"].get("combined"),
            defence_sacks=os["defense"].get("sacks"),
            defence_sack_yards=os["defense"].get("sack_yards"),
            defence_interceptions=os["defense"].get("interceptions"),
            defence_passes_defended=os["defense"].get("passes_defended"),
            defence_forced_fumbles=os["defense"].get("forced_fumbles"),
            defence_fumble_recoveries=os["defense"].get("fumble_recoveries"),
            defence_qb_hits=os["defense"].get("qb_hits"),
            defence_tloss=os["defense"].get("tloss"),
            defence_tloss_yards=os["defense"].get("tloss_yards"),
            defence_safeties=os["defense"].get("safeties"),
            defence_sp_tackles=os["defense"].get("sp_tackles"),
            defence_sp_assists=os["defense"].get("sp_assists"),
            defence_sp_forced_fumbles=os["defense"].get("sp_forced_fumbles"),
            defence_sp_fumble_recoveries=os["defense"].get("sp_fumble_recoveries"),
            defence_sp_blocks=os["defense"].get("sp_blocks"),
            defence_misc_tackles=os["defense"].get("misc_tackles"),
            defence_misc_assists=os["defense"].get("misc_assists"),
            defence_misc_forced_fumbles=os["defense"].get("misc_forced_fumbles"),
            defence_misc_fumble_recoveries=os["defense"].get("misc_fumble_recoveries"),
            defence_def_targets=os["defense"].get("def_targets"),
            defence_def_comps=os["defense"].get("def_comps"),
            defence_blitzes=os["defense"].get("blitzes"),
            defence_hurries=os["defense"].get("hurries"),
            defence_knockdowns=os["defense"].get("knockdowns"),
            defence_missed_tackles=os["defense"].get("missed_tackles"),
            defence_batted_passes=os["defense"].get("batted_passes"),
            defence_three_and_outs_forced=os["defense"].get("three_and_outs_forced"),
            defence_fourth_down_stops=os["defense"].get("fourth_down_stops"),
            extra_points_kicks_attempts=os["extra_points"]["kicks"].get("attempts"),
            extra_points_kicks_blocked=os["extra_points"]["kicks"].get("blocked"),
            extra_points_kicks_made=os["extra_points"]["kicks"].get("made"),
            extra_points_kicks_pct=os["extra_points"]["kicks"].get("pct"),
            extra_points_conversions_pass_attempts=os["extra_points"][
                "conversions"
            ].get("pass_attempts"),
            extra_points_conversions_pass_successes=os["extra_points"][
                "conversions"
            ].get("pass_successes"),
            extra_points_conversions_rush_attempts=os["extra_points"][
                "conversions"
            ].get("rush_attempts"),
            extra_points_conversions_rush_successes=os["extra_points"][
                "conversions"
            ].get("rush_successes"),
            extra_points_conversions_defense_attempts=os["extra_points"][
                "conversions"
            ].get("defense_attempts"),
            extra_points_conversions_defense_successes=os["extra_points"][
                "conversions"
            ].get("defense_successes"),
            extra_points_conversions_turnover_successes=os["extra_points"][
                "conversions"
            ].get("turnover_successes"),
            efficiency_goaltogo_attempts=os["efficiency"]["goaltogo"].get("attempts"),
            efficiency_goaltogo_successes=os["efficiency"]["goaltogo"].get("successes"),
            efficiency_goaltogo_pct=os["efficiency"]["goaltogo"].get("pct"),
            efficiency_redzone_attempts=os["efficiency"]["redzone"].get("attempts"),
            efficiency_redzone_successes=os["efficiency"]["redzone"].get("successes"),
            efficiency_redzone_pct=os["efficiency"]["redzone"].get("pct"),
            efficiency_thirddown_attempts=os["efficiency"]["thirddown"].get("attempts"),
            efficiency_thirddown_successes=os["efficiency"]["thirddown"].get(
                "successes"
            ),
            efficiency_thirddown_pct=os["efficiency"]["thirddown"].get("pct"),
            efficiency_fourthdown_attempts=os["efficiency"]["fourthdown"].get(
                "attempts"
            ),
            efficiency_fourthdown_successes=os["efficiency"]["fourthdown"].get(
                "successes"
            ),
            efficiency_fourthdown_pct=os["efficiency"]["fourthdown"].get("pct"),
        )
        team_stats_final.append(team_stats_for)
        team_stats_final.append(team_stats_opponent)
    return team_stats_final


@router.post("/team_season_stats/{season_year}/{season_type}")
async def batch_insert_season_team_statistics(season_year: int, season_type: str):
    # Batch insert the List[TeamSeasonStats] for a specific season type and year    #
    #                                                                               #
    # Return a success string to signify successful entry                           #

    all_teams_season_stats = []
    try:
        all_teams_season_stats = await fetch_team_season_stats(season_year, season_type)
    except Exception as ex:
        print(
            f"Could not fetch season stats for teams of {season_year}-{season_type}: {ex}"
        )
        raise Exception
    try:
        insert_value = await bulk_insert_all_teams_season_stats(all_teams_season_stats)
    except Exception as ex:
        print(
            f"Could not fetch season stats for teams of {season_year}-{season_type}: {ex}"
        )
        raise Exception

    return insert_value
