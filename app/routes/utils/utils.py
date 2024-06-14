from app.models.team_game_statistics import TeamGameStats


def generate_teamgamestat_model(
    general_game_db, stats, season_year, season_type, isHome: bool
):
    identifiers = {
        "game_id_db": general_game_db.id,
        "game_api_id": general_game_db.game_api_id,
        "home_team_id_db": general_game_db.home_team_id,
        "home_team_id_api": general_game_db.home_team_api_id,
        "away_team_id_db": general_game_db.away_team_id,
        "away_team_id_api": general_game_db.away_team_api_id,
        "season_year": season_year,
        "season_type": season_type,
    }

    # Foreign Key values for away team
    team_id = identifiers["home_team_id_db"]
    team_api_id = identifiers["home_team_id_api"]

    # Foreign Key values for away team
    if not isHome:
        team_id = identifiers["away_team_id_db"]
        team_api_id = identifiers["away_team_id_api"]

    team_game_stats = TeamGameStats(
        game_id=identifiers["game_id_db"],
        team_id=team_id,
        team_api_id=team_api_id,
        season_year=identifiers["season_year"],
        season_type=identifiers["season_type"],
        summary_possession_time=stats["summary"]["possession_time"],
        summary_avg_gain=stats["summary"]["avg_gain"],
        summary_safeties=stats["summary"]["safeties"],
        summary_turnovers=stats["summary"]["turnovers"],
        summary_play_count=stats["summary"]["play_count"],
        summary_rush_plays=stats["summary"]["rush_plays"],
        summary_total_yards=stats["summary"]["total_yards"],
        summary_fumbles=stats["summary"]["fumbles"],
        summary_lost_fumbles=stats["summary"]["lost_fumbles"],
        summary_penalties=stats["summary"]["penalties"],
        summary_penalty_yards=stats["summary"]["penalty_yards"],
        summary_return_yards=stats["summary"]["return_yards"],
        rushing_avg_yards=stats["rushing"]["totals"].get("avg_yards"),
        rushing_attempts=stats["rushing"]["totals"].get("attempts"),
        rushing_touchdowns=stats["rushing"]["totals"].get("touchdowns"),
        rushing_tlost=stats["rushing"]["totals"].get("tlost"),
        rushing_tlost_yards=stats["rushing"]["totals"].get("tlost_yards"),
        rushing_yards=stats["rushing"]["totals"].get("yards"),
        rushing_longest=stats["rushing"]["totals"].get("longest"),
        rushing_longest_touchdown=stats["rushing"]["totals"].get("longest_touchdown"),
        rushing_redzone_attempts=stats["rushing"]["totals"].get("redzone_attempts"),
        rushing_brocken_tackles=stats["rushing"]["totals"].get("broken_tackles"),
        rushing_kneel_downs=stats["rushing"]["totals"].get("kneel_downs"),
        rushing_scrambles=stats["rushing"]["totals"].get("scrambles"),
        rushing_yards_after_contact=stats["rushing"]["totals"].get(
            "yards_after_contact"
        ),
        rushing_first_downs=stats["rushing"]["totals"].get("yards_after_contact"),
        receiving_targets=stats["receiving"]["totals"].get("targets"),
        receiving_receptions=stats["receiving"]["totals"].get("receptions"),
        receiving_avg_yards=stats["receiving"]["totals"].get("avg_yards"),
        receiving_yards=stats["receiving"]["totals"].get("yards"),
        receiving_touchdowns=stats["receiving"]["totals"].get("touchdowns"),
        receiving_yards_after_catch=stats["receiving"]["totals"].get(
            "yards_after_catch"
        ),
        receiving_longest=stats["receiving"]["totals"].get("longest"),
        receiving_longest_touchdown=stats["receiving"]["totals"].get(
            "longest_touchdown"
        ),
        receiving_redzone_targets=stats["receiving"]["totals"].get("redzone_targets"),
        receiving_air_yards=stats["receiving"]["totals"].get("air_yards"),
        receiving_broken_tackles=stats["receiving"]["totals"].get("broken_tackles"),
        receiving_dropped_passes=stats["receiving"]["totals"].get("dropped_passes"),
        receiving_catchable_passes=stats["receiving"]["totals"].get("catchable_passes"),
        receiving_yards_after_contact=stats["receiving"]["totals"].get(
            "yards_after_contact"
        ),
        receiving_first_downs=stats["receiving"]["totals"].get("first_downs"),
        passing_attempts=stats["passing"]["totals"].get("attempts"),
        passing_completions=stats["passing"]["totals"].get("completions"),
        passing_cmp_pct=stats["passing"]["totals"].get("cmp_pct"),
        passing_interceptions=stats["passing"]["totals"].get("interceptions"),
        passing_sack_yards=stats["passing"]["totals"].get("sack_yards"),
        passing_rating=stats["passing"]["totals"].get("rating"),
        passing_touchdowns=stats["passing"]["totals"].get("touchdowns"),
        passing_avg_yards=stats["passing"]["totals"].get("avg_yards"),
        passing_sacks=stats["passing"]["totals"].get("sacks"),
        passing_longest=stats["passing"]["totals"].get("longest"),
        passing_longest_touchdown=stats["passing"]["totals"].get("longest_touchdown"),
        passing_air_yards=stats["passing"]["totals"].get("air_yards"),
        passing_redzone_attempts=stats["passing"]["totals"].get("redzone_attempts"),
        passing_net_yards=stats["passing"]["totals"].get("net_yards"),
        passing_yards=stats["passing"]["totals"].get("yards"),
        passing_int_touchdowns=stats["passing"]["totals"].get("int_touchdowns"),
        passing_throw_aways=stats["passing"]["totals"].get("throw_aways"),
        passing_poor_throws=stats["passing"]["totals"].get("poor_throws"),
        passing_defended_passes=stats["passing"]["totals"].get("defended_passes"),
        passing_dropped_passes=stats["passing"]["totals"].get("dropped_passes"),
        passing_spikes=stats["passing"]["totals"].get("spikes"),
        passing_blitzes=stats["passing"]["totals"].get("blitzes"),
        passing_hurries=stats["passing"]["totals"].get("hurries"),
        passing_knockdowns=stats["passing"]["totals"].get("knockdowns"),
        passing_pocket_time=stats["passing"]["totals"].get("pocket_time"),
        passing_batted_passes=stats["passing"]["totals"].get("batted_passes"),
        passing_on_target_throws=stats["passing"]["totals"].get("on_target_throws"),
        passing_first_downs=stats["passing"]["totals"].get("first_downs"),
        defence_tackles=stats["defense"]["totals"].get("tackles"),
        defence_assists=stats["defense"]["totals"].get("assists"),
        defence_combined=stats["defense"]["totals"].get("combined"),
        defence_sacks=stats["defense"]["totals"].get("sacks"),
        defence_sack_yards=stats["defense"]["totals"].get("sack_yards"),
        defence_interceptions=stats["defense"]["totals"].get("interceptions"),
        defence_passes_defended=stats["defense"]["totals"].get("passes_defended"),
        defence_forced_fumbles=stats["defense"]["totals"].get("forced_fumbles"),
        defence_fumble_recoveries=stats["defense"]["totals"].get("fumble_recoveries"),
        defence_qb_hits=stats["defense"]["totals"].get("qb_hits"),
        defence_tloss=stats["defense"]["totals"].get("tloss"),
        defence_tloss_yards=stats["defense"]["totals"].get("tloss_yards"),
        defence_safeties=stats["defense"]["totals"].get("safeties"),
        defence_sp_tackles=stats["defense"]["totals"].get("sp_tackles"),
        defence_sp_assists=stats["defense"]["totals"].get("sp_assists"),
        defence_sp_forced_fumbles=stats["defense"]["totals"].get("sp_forced_fumbles"),
        defence_sp_fumble_recoveries=stats["defense"]["totals"].get(
            "sp_fumble_recoveries"
        ),
        defence_sp_blocks=stats["defense"]["totals"].get("sp_blocks"),
        defence_misc_tackles=stats["defense"]["totals"].get("misc_tackles"),
        defence_misc_assists=stats["defense"]["totals"].get("misc_assists"),
        defence_misc_forced_fumbles=stats["defense"]["totals"].get(
            "misc_forced_fumbles"
        ),
        defence_misc_fumble_recoveries=stats["defense"]["totals"].get(
            "misc_fumble_recoveries"
        ),
        defence_def_targets=stats["defense"]["totals"].get("def_targets"),
        defence_def_comps=stats["defense"]["totals"].get("def_comps"),
        defence_blitzes=stats["defense"]["totals"].get("blitzes"),
        defence_hurries=stats["defense"]["totals"].get("hurries"),
        defence_knockdowns=stats["defense"]["totals"].get("knockdowns"),
        defence_missed_tackles=stats["defense"]["totals"].get("missed_tackles"),
        defence_batted_passes=stats["defense"]["totals"].get("batted_passes"),
        defence_three_and_outs_forced=stats["defense"]["totals"].get(
            "three_and_outs_forced"
        ),
        defence_fourth_down_stops=stats["defense"]["totals"].get("fourth_down_stops"),
        efficiency_goaltogo_attempts=stats["efficiency"]["goaltogo"].get("attempts"),
        efficiency_goaltogo_successes=stats["efficiency"]["goaltogo"].get("successes"),
        efficiency_goaltogo_pct=stats["efficiency"]["goaltogo"].get("pct"),
        efficiency_redzone_attempts=stats["efficiency"]["redzone"].get("attempts"),
        efficiency_redzone_successes=stats["efficiency"]["redzone"].get("successes"),
        efficiency_redzone_pct=stats["efficiency"]["redzone"].get("pct"),
        efficiency_thirddown_attempts=stats["efficiency"]["thirddown"].get("attempts"),
        efficiency_thirddown_successes=stats["efficiency"]["thirddown"].get(
            "successes"
        ),
        efficiency_thirddown_pct=stats["efficiency"]["thirddown"].get("pct"),
        efficiency_fourthdown_attempts=stats["efficiency"]["fourthdown"].get(
            "attempts"
        ),
        efficiency_fourthdown_successes=stats["efficiency"]["fourthdown"].get(
            "successes"
        ),
        efficiency_fourthdown_pct=stats["efficiency"]["fourthdown"].get("pct"),
        touchdown_passes=stats["touchdowns"].get("pass"),
        touchdown_rushes=stats["touchdowns"].get("rush"),
        touchdown_total_return=stats["touchdowns"].get("total_return"),
        touchdown_total=stats["touchdowns"].get("total"),
        touchdown_fumble_return=stats["touchdowns"].get("fumble_return"),
        touchdown_int_return=stats["touchdowns"].get("int_return"),
        touchdown_kick_return=stats["touchdowns"].get("kick_return"),
        touchdown_point_return=stats["touchdowns"].get("punt_return"),
        touchdown_other=stats["touchdowns"].get("other"),
        first_downs_pass=stats["first_downs"].get("pass"),
        first_downs_penalty=stats["first_downs"].get("penalty"),
        first_downs_rush=stats["first_downs"].get("rush"),
        first_downs_total=stats["first_downs"].get("total"),
        kickoffs_endzone=stats["kickoffs"]["totals"].get("endzone"),
        kickoffs_inside_20=stats["kickoffs"]["totals"].get("inside_20"),
        kickoffs_return_yards=stats["kickoffs"]["totals"].get("return_yards"),
        kickoffs_touchbacks=stats["kickoffs"]["totals"].get("touchbacks"),
        kickoffs_yards=stats["kickoffs"]["totals"].get("yards"),
        kickoffs_out_of_bounds=stats["kickoffs"]["totals"].get("out_of_bounds"),
        kickoffs_number=stats["kickoffs"]["totals"].get("number"),
        kickoffs_onside_successes=stats["kickoffs"]["totals"].get("onside_attempts"),
        kickoffs_onside_attempts=stats["kickoffs"]["totals"].get("onside_successes"),
        kickoffs_squib_kicks=stats["kickoffs"]["totals"].get("squib_kicks"),
        kickoffs_total_endzone=stats["kickoffs"]["totals"].get("total_endzone"),
    )
    if stats.get("penalties"):
        team_game_stats.penalties_first_downs = (
            stats["penalties"]["totals"].get("first_downs"),
        )
        team_game_stats.penalties_penalties = (
            stats["penalties"]["totals"].get("penalties"),
        )
        team_game_stats.penalties_yards = (stats["penalties"]["totals"].get("yards"),)
    if stats.get("punts"):
        team_game_stats.punts_attempts = (stats["punts"]["totals"].get("attempts"),)
        team_game_stats.punts_yards = (stats["punts"]["totals"].get("yards"),)
        team_game_stats.punts_net_yards = (stats["punts"]["totals"].get("net_yards"),)
        team_game_stats.punts_blocked = (stats["punts"]["totals"].get("blocked"),)
        team_game_stats.punts_touchbacks = (stats["punts"]["totals"].get("touchbacks"),)
        team_game_stats.punts_inside_20 = (stats["punts"]["totals"].get("inside_20"),)
        team_game_stats.punts_return_yards = (
            stats["punts"]["totals"].get("return_yards"),
        )
        team_game_stats.punts_avg_net_yards = (
            stats["punts"]["totals"].get("avg_net_yards"),
        )
        team_game_stats.punts_avg_yards = (stats["punts"]["totals"].get("avg_yards"),)
        team_game_stats.punts_longest = (stats["punts"]["totals"].get("longest"),)
        team_game_stats.punts_hang_time = (stats["punts"]["totals"].get("hang_time"),)
        team_game_stats.punts_avg_hang_time = (
            stats["punts"]["totals"].get("avg_hang_time"),
        )
    if stats.get("punt_returns"):
        team_game_stats.punt_returns_avg_yards = (
            stats["punt_returns"]["totals"].get("avg_yards"),
        )
        team_game_stats.punt_returns_yards = (
            stats["punt_returns"]["totals"].get("yards"),
        )
        team_game_stats.punt_returns_longest = (
            stats["punt_returns"]["totals"].get("longest"),
        )
        team_game_stats.punt_returns_touchdowns = (
            stats["punt_returns"]["totals"].get("touchdowns"),
        )
        team_game_stats.punt_returns_longest_touchdown = (
            stats["punt_returns"]["totals"].get("longest_touchdown"),
        )
        team_game_stats.punt_returns_faircatches = (
            stats["punt_returns"]["totals"].get("faircatches"),
        )
        team_game_stats.punt_returns_number = (
            stats["punt_returns"]["totals"].get("number"),
        )
    if stats.get("field_goals"):
        team_game_stats.field_goals_attempts = (
            stats["field_goals"]["totals"].get("attempts"),
        )
        team_game_stats.field_goals_made = (stats["field_goals"]["totals"].get("made"),)
        team_game_stats.field_goals_blocked = (
            stats["field_goals"]["totals"].get("blocked"),
        )
        team_game_stats.field_goals_yards = (
            stats["field_goals"]["totals"].get("yards"),
        )
        team_game_stats.field_goals_avg_yards = (
            stats["field_goals"]["totals"].get("avg_yards"),
        )
        team_game_stats.field_goals_longest = (
            stats["field_goals"]["totals"].get("longest"),
        )
        team_game_stats.field_goals_missed = (
            stats["field_goals"]["totals"].get("missed"),
        )
        team_game_stats.field_goals_pct = (stats["field_goals"]["totals"].get("pct"),)
        team_game_stats.field_goals_attempts_19 = (
            stats["field_goals"]["totals"].get("attempts_19"),
        )
        team_game_stats.field_goals_attempts_29 = (
            stats["field_goals"]["totals"].get("attempts_29"),
        )
        team_game_stats.field_goals_attempts_39 = (
            stats["field_goals"]["totals"].get("attempts_39"),
        )
        team_game_stats.field_goals_attempts_49 = (
            stats["field_goals"]["totals"].get("attempts_49"),
        )
        team_game_stats.field_goals_attempts_50 = (
            stats["field_goals"]["totals"].get("attempts_50"),
        )
        team_game_stats.field_goals_made_19 = (
            stats["field_goals"]["totals"].get("made_19"),
        )
        team_game_stats.field_goals_made_29 = (
            stats["field_goals"]["totals"].get("made_29"),
        )
        team_game_stats.field_goals_made_39 = (
            stats["field_goals"]["totals"].get("made_39"),
        )
        team_game_stats.field_goals_made_49 = (
            stats["field_goals"]["totals"].get("made_49"),
        )
        team_game_stats.field_goals_made_50 = (
            stats["field_goals"]["totals"].get("made_50"),
        )
    if stats.get("fumbles"):
        team_game_stats.fumbles_fumbles = (stats["fumbles"]["totals"].get("fumbles"),)
        team_game_stats.fumbles_lost_fumbles = (
            stats["fumbles"]["totals"].get("lost_fumbles"),
        )
        team_game_stats.fumbles_own_rec = (stats["fumbles"]["totals"].get("own_rec"),)
        team_game_stats.fumbles_own_rec_yards = (
            stats["fumbles"]["totals"].get("own_rec_yards"),
        )
        team_game_stats.fumbles_opp_rec = (stats["fumbles"]["totals"].get("opp_rec"),)
        team_game_stats.fumbles_out_of_bounds = (
            stats["fumbles"]["totals"].get("out_of_bounds"),
        )
        team_game_stats.fumbles_forced_fumbles = (
            stats["fumbles"]["totals"].get("forced_fumbles"),
        )
        team_game_stats.fumbles_own_rec_tds = (
            stats["fumbles"]["totals"].get("own_rec_tds"),
        )
        team_game_stats.fumbles_opp_rec_tds = (
            stats["fumbles"]["totals"].get("opp_rec_tds"),
        )
        team_game_stats.fumbles_ez_rec_tds = (
            stats["fumbles"]["totals"].get("ez_rec_tds"),
        )
    if stats.get("kick_returns"):
        team_game_stats.kick_returns_avg_yards = (
            stats["kick_returns"]["totals"].get("avg_yards"),
        )
        team_game_stats.kick_returns_yards = (
            stats["kick_returns"]["totals"].get("yards"),
        )
        team_game_stats.kick_returns_longest = (
            stats["kick_returns"]["totals"].get("longest"),
        )
        team_game_stats.kick_returns_touchdowns = (
            stats["kick_returns"]["totals"].get("touchdowns"),
        )
        team_game_stats.kick_returns_longest_touchdown = (
            stats["kick_returns"]["totals"].get("longest_touchdown"),
        )
        team_game_stats.kick_returns_faircatches = (
            stats["kick_returns"]["totals"].get("faircatches"),
        )
        team_game_stats.kick_returns_number = (
            stats["kick_returns"]["totals"].get("number"),
        )
    if stats.get("int_returns"):
        team_game_stats.int_returns_avg_yards = (
            stats["int_returns"]["totals"].get("avg_yards"),
        )
        team_game_stats.int_returns_yards = (
            stats["int_returns"]["totals"].get("yards"),
        )
        team_game_stats.int_returns_longest = (
            stats["int_returns"]["totals"].get("longest"),
        )
        team_game_stats.int_returns_touchdowns = (
            stats["int_returns"]["totals"].get("touchdowns"),
        )
        team_game_stats.int_returns_longest_touchdown = (
            stats["int_returns"]["totals"].get("longest_touchdown"),
        )
        team_game_stats.int_returns_number = (
            stats["int_returns"]["totals"].get("number"),
        )
    if stats.get("interceptions"):
        team_game_stats.interceptions_return_yards = stats.get("interceptions").get(
            "return_yards"
        )
        team_game_stats.interceptions_returned = stats.get("interceptions").get(
            "returned"
        )
        team_game_stats.interceptions_number = stats.get("interceptions").get("number")
    if stats.get("extra_points"):
        team_game_stats.extra_points_kicks_attempts = (
            stats["extra_points"]["kicks"]["totals"].get("attempts"),
        )
        team_game_stats.extra_points_kicks_blocked = (
            stats["extra_points"]["kicks"]["totals"].get("blocked"),
        )
        team_game_stats.extra_points_kicks_made = (
            stats["extra_points"]["kicks"]["totals"].get("made"),
        )
        team_game_stats.extra_points_kicks_pct = (
            stats["extra_points"]["kicks"]["totals"].get("pct"),
        )
        team_game_stats.extra_points_conversions_pass_attempts = (
            stats["extra_points"]["conversions"]["totals"].get("pass_attempts"),
        )
        team_game_stats.extra_points_conversions_pass_successes = (
            stats["extra_points"]["conversions"]["totals"].get("pass_successes"),
        )
        team_game_stats.extra_points_conversions_rush_attempts = (
            stats["extra_points"]["conversions"]["totals"].get("rush_attempts"),
        )
        team_game_stats.extra_points_conversions_rush_successes = (
            stats["extra_points"]["conversions"]["totals"].get("rush_successes"),
        )
        team_game_stats.extra_points_conversions_defense_attempts = (
            stats["extra_points"]["conversions"]["totals"].get("defense_attempts"),
        )
        team_game_stats.extra_points_conversions_defense_successes = (
            stats["extra_points"]["conversions"]["totals"].get("defense_successes"),
        )
        team_game_stats.extra_points_conversions_turnover_successes = (
            stats["extra_points"]["conversions"]["totals"].get("turnover_successes"),
        )

    return team_game_stats
