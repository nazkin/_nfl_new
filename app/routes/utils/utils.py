from app.models.team_game_statistics import TeamGameStats
from app.models.player_game_statistics import PlayerGameStats
from app.models.player_season_statistics import PlayerSeasonStats
from app.models.teams_profile import TeamsProfile
from app.routes.utils.small_helpers import insert_non_existing_player

# Generates a PlayerSeasonStats model from JSON data
def generate_playerseasonstats_model(player, general_stats, player_db, s_y, s_t):
    p_model = PlayerSeasonStats(
        player_api_id=player.get("id"),
        team_id=general_stats["team_id_db"],
        team_api_id=general_stats["team_api_id"],
        season_year=s_y,
        season_type=s_t,
        games_played=player.get("games_played"),
        games_started=player.get("games_started"),
        player_name=player.get("name"),
        player_jersey=player.get("jersey"),
        player_position=player.get("position "),
    )

    if player_db:
        p_model.player_id = (player_db.id,)
    else:
        # This player was not part of the roster so we insert him before storing
        p_model.player_id = insert_non_existing_player(p_model)

    if player.get("rushing"):
        p_model.rushing_avg_yards = player["rushing"].get("avg_yards")
        p_model.rushing_attempts = player["rushing"].get("attempts")
        p_model.rushing_touchdowns = player["rushing"].get("touchdowns")
        p_model.rushing_tlost = player["rushing"].get("tlost")
        p_model.rushing_tlost_yards = player["rushing"].get("tlost_yards")
        p_model.rushing_yards = player["rushing"].get("yards")
        p_model.rushing_longest = player["rushing"].get("longest")
        p_model.rushing_longest_touchdown = player["rushing"].get("longest_touchdown")
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
        p_model.receiving_redzone_targets = player["receiving"].get("redzone_targets")
        p_model.receiving_air_yards = player["receiving"].get("air_yards")
        p_model.receiving_broken_tackles = player["receiving"].get("broken_tackles")
        p_model.receiving_dropped_passes = player["receiving"].get("dropped_passes")
        p_model.receiving_catchable_passes = player["receiving"].get("catchable_passes")
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
        p_model.passing_longest_touchdown = player["passing"].get("longest_touchdown")
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
        p_model.kickoffs_onside_successes = player["kickoffs"].get("onside_attempts")
        p_model.kickoffs_onside_attempts = player["kickoffs"].get("onside_successes")
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
        p_model.kick_returns_touchdowns = (player["kick_returns"].get("touchdowns"),)
        p_model.kick_returns_longest_touchdown = (
            player["kick_returns"].get("longest_touchdown"),
        )
        p_model.kick_returns_faircatches = (player["kick_returns"].get("faircatches"),)
        p_model.kick_returns_returns = (player["kick_returns"].get("returns"),)
    else:
        p_model.kick_returns_avg_yards = None
        p_model.kick_returns_yards = None
        p_model.kick_returns_longest = None
        p_model.kick_returns_touchdowns = None
        p_model.kick_returns_longest_touchdown = None
        p_model.kick_returns_faircatches = None
        p_model.kick_returns_returns = None

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
        p_model.field_goals_attempts_19 = (player["field_goals"].get("attempts_19"),)
        p_model.field_goals_attempts_29 = (player["field_goals"].get("attempts_29"),)
        p_model.field_goals_attempts_39 = (player["field_goals"].get("attempts_39"),)
        p_model.field_goals_attempts_49 = (player["field_goals"].get("attempts_49"),)
        p_model.field_goals_attempts_50 = (player["field_goals"].get("attempts_50"),)
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

    if player.get("defense"):
        p_model.defence_tackles = (player["defense"].get("tackles"),)
        p_model.defence_assists = (player["defense"].get("assists"),)
        p_model.defence_combined = (player["defense"].get("combined"),)
        p_model.defence_sacks = (player["defense"].get("sacks"),)
        p_model.defence_sack_yards = (player["defense"].get("sack_yards"),)
        p_model.defence_interceptions = (player["defense"].get("interceptions"),)
        p_model.defence_passes_defended = (player["defense"].get("passes_defended"),)
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
        p_model.extra_points_kicks_attempts = (player["extra_points"].get("attempts"),)
        p_model.extra_points_kicks_blocked = (player["extra_points"].get("blocked"),)
        p_model.extra_points_kicks_made = (player["extra_points"].get("made"),)
        p_model.extra_points_kicks_pct = (player["extra_points"].get("pct"),)
    else:
        p_model.extra_points_kicks_attempts = None
        p_model.extra_points_kicks_blocked = None
        p_model.extra_points_kicks_made = None
        p_model.extra_points_kicks_pct = None

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

    return p_model


# Generates a TeamsProfile model from JSON data
def generate_teamprofile_model(tp: dict, api_id: str):
    teams_profile = TeamsProfile(
        team_api_id=api_id,
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

    return teams_profile


# Generates a TeamGameStats model from JSON data
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

    # Foreign Key values for home team
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


# Generates a PlayerGameStats model from JSON data
def generate_playergamestat_model(stat_list):
    all_game_stats = []

    if len(stat_list["rushing"]) > 0:
        for p_stats in stat_list["rushing"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                rushing_avg_yards=p_stats.get("avg_yards"),
                rushing_attempts=p_stats.get("attempts"),
                rushing_touchdowns=p_stats.get("touchdowns"),
                rushing_tlost=p_stats.get("tlost"),
                rushing_tlost_yards=p_stats.get("tlost_yards"),
                rushing_yards=p_stats.get("yards"),
                rushing_longest=p_stats.get("longest"),
                rushing_longest_touchdown=p_stats.get("longest_touchdown"),
                rushing_redzone_attempts=p_stats.get("redzone_attempts"),
                rushing_broken_tackles=p_stats.get("broken_tackles"),
                rushing_kneel_downs=p_stats.get("kneel_downs"),
                rushing_scrambles=p_stats.get("scrambles"),
                rushing_yards_after_contact=p_stats.get("yards_after_contact"),
                rushing_first_down=p_stats.get("first_downs"),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["receiving"]) > 0:
        for p_stats in stat_list["receiving"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                receiving_targets=p_stats.get("targets"),
                receiving_receptions=p_stats.get("receptions"),
                receiving_avg_yards=p_stats.get("avg_yards"),
                receiving_yards=p_stats.get("yards"),
                receiving_touchdowns=p_stats.get("touchdowns"),
                receiving_yards_after_catch=p_stats.get("yards_after_catch"),
                receiving_longest=p_stats.get("longest"),
                receiving_longest_touchdown=p_stats.get("longest_touchdown"),
                receiving_redzone_targets=p_stats.get("redzone_targets"),
                receiving_air_yards=p_stats.get("air_yards"),
                receiving_broken_tackles=p_stats.get("broken_tackles"),
                receiving_dropped_passes=p_stats.get("dropped_passes"),
                receiving_catchable_passes=p_stats.get("catchable_passes"),
                receiving_yards_after_contact=p_stats.get("yards_after_contact"),
                receiving_first_downs=p_stats.get("first_downs"),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["punts"]) > 0:
        for p_stats in stat_list["punts"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                punts_attempts=(p_stats.get("attempts"),),
                punts_yards=(p_stats.get("yards"),),
                punts_net_yards=(p_stats.get("net_yards"),),
                punts_blocked=(p_stats.get("blocked"),),
                punts_touchbacks=(p_stats.get("touchbacks"),),
                punts_inside_20=(p_stats.get("inside_20"),),
                punts_return_yards=(p_stats.get("return_yards")),
                punts_avg_net_yards=(p_stats.get("avg_net_yards"),),
                punts_avg_yards=(p_stats.get("avg_yards"),),
                punts_longest=(p_stats.get("longest"),),
                punts_hang_time=(p_stats.get("hang_time"),),
                punts_avg_hang_time=(p_stats.get("avg_hang_time"),),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["punt_returns"]) > 0:
        for p_stats in stat_list["punt_returns"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                punt_returns_avg_yards=(p_stats.get("avg_yards"),),
                punt_returns_yards=(p_stats.get("yards"),),
                punt_returns_longest=(p_stats.get("longest"),),
                punt_returns_touchdowns=(p_stats.get("touchdowns"),),
                punt_returns_longest_touchdown=(p_stats.get("longest_touchdown"),),
                punt_returns_faircatches=(p_stats.get("faircatches"),),
                punt_returns_number=(p_stats.get("number"),),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["penalties"]) > 0:
        for p_stats in stat_list["penalties"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                penalties_first_downs=(p_stats.get("first_downs"),),
                penalties_penalties=(p_stats.get("penalties"),),
                penalties_yards=(p_stats.get("yards"),),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["passing"]) > 0:
        for p_stats in stat_list["passing"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                passing_attempts=p_stats.get("attempts"),
                passing_completions=p_stats.get("completions"),
                passing_cmp_pct=p_stats.get("cmp_pct"),
                passing_interceptions=p_stats.get("interceptions"),
                passing_sack_yards=p_stats.get("sack_yards"),
                passing_rating=p_stats.get("rating"),
                passing_touchdowns=p_stats.get("touchdowns"),
                passing_avg_yards=p_stats.get("avg_yards"),
                passing_sacks=p_stats.get("sacks"),
                passing_longest=p_stats.get("longest"),
                passing_longest_touchdown=p_stats.get("longest_touchdown"),
                passing_air_yards=p_stats.get("air_yards"),
                passing_redzone_attempts=p_stats.get("redzone_attempts"),
                passing_net_yards=p_stats.get("net_yards"),
                passing_yards=p_stats.get("yards"),
                passing_int_touchdowns=p_stats.get("int_touchdowns"),
                passing_throw_aways=p_stats.get("throw_aways"),
                passing_poor_throws=p_stats.get("poor_throws"),
                passing_defended_passes=p_stats.get("defended_passes"),
                passing_dropped_passes=p_stats.get("dropped_passes"),
                passing_spikes=p_stats.get("spikes"),
                passing_blitzes=p_stats.get("blitzes"),
                passing_hurries=p_stats.get("hurries"),
                passing_knockdowns=p_stats.get("knockdowns"),
                passing_pocket_time=p_stats.get("pocket_time"),
                passing_batted_passes=p_stats.get("batted_passes"),
                passing_on_target_throws=p_stats.get("on_target_throws"),
                passing_first_downs=p_stats.get("first_downs"),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["kickoffs"]) > 0:
        for p_stats in stat_list["kickoffs"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                kickoffs_endzone=p_stats.get("endzone"),
                kickoffs_inside_20=p_stats.get("inside_20"),
                kickoffs_return_yards=p_stats.get("return_yards"),
                kickoffs_touchbacks=p_stats.get("touchbacks"),
                kickoffs_yards=p_stats.get("yards"),
                kickoffs_out_of_bounds=p_stats.get("out_of_bounds"),
                kickoffs_number=p_stats.get("number"),
                kickoffs_onside_successes=p_stats.get("onside_attempts"),
                kickoffs_onside_attempts=p_stats.get("onside_successes"),
                kickoffs_squib_kicks=p_stats.get("squib_kicks"),
                kickoffs_total_endzone=p_stats.get("total_endzone"),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["kick_returns"]) > 0:
        for p_stats in stat_list["kick_returns"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                kick_returns_avg_yards=(p_stats.get("avg_yards"),),
                kick_returns_yards=(p_stats.get("yards"),),
                kick_returns_longest=(p_stats.get("longest"),),
                kick_returns_touchdowns=(p_stats.get("touchdowns"),),
                kick_returns_longest_touchdown=(p_stats.get("longest_touchdown"),),
                kick_returns_faircatches=(p_stats.get("faircatches"),),
                kick_returns_number=(p_stats.get("number"),),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["int_returns"]) > 0:
        for p_stats in stat_list["int_returns"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                int_returns_avg_yards=(p_stats.get("avg_yards"),),
                int_returns_yards=(p_stats.get("yards"),),
                int_returns_longest=(p_stats.get("longest"),),
                int_returns_touchdowns=(p_stats.get("touchdowns"),),
                int_returns_longest_touchdown=(p_stats.get("longest_touchdown"),),
                int_returns_number=(p_stats.get("number"),),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["fumbles"]) > 0:
        for p_stats in stat_list["fumbles"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                fumbles_fumbles=(p_stats.get("fumbles"),),
                fumbles_lost_fumbles=(p_stats.get("lost_fumbles"),),
                fumbles_own_rec=(p_stats.get("own_rec"),),
                fumbles_own_rec_yards=(p_stats.get("own_rec_yards"),),
                fumbles_opp_rec=(p_stats.get("opp_rec"),),
                fumbles_out_of_bounds=(p_stats.get("out_of_bounds"),),
                fumbles_forced_fumbles=(p_stats.get("forced_fumbles"),),
                fumbles_own_rec_tds=(p_stats.get("own_rec_tds"),),
                fumbles_opp_rec_tds=(p_stats.get("opp_rec_tds"),),
                fumbles_ez_rec_tds=(p_stats.get("ez_rec_tds"),),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["field_goals"]) > 0:
        for p_stats in stat_list["field_goals"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                field_goals_attempts=(p_stats.get("attempts"),),
                field_goals_made=(p_stats.get("made"),),
                field_goals_blocked=(p_stats.get("blocked"),),
                field_goals_yards=(p_stats.get("yards"),),
                field_goals_avg_yards=(p_stats.get("avg_yards"),),
                field_goals_longest=(p_stats.get("longest"),),
                field_goals_missed=(p_stats.get("missed"),),
                field_goals_pct=(p_stats.get("pct"),),
                field_goals_attempts_19=(p_stats.get("attempts_19"),),
                field_goals_attempts_29=(p_stats.get("attempts_29"),),
                field_goals_attempts_39=(p_stats.get("attempts_39"),),
                field_goals_attempts_49=(p_stats.get("attempts_49"),),
                field_goals_attempts_50=(p_stats.get("attempts_50"),),
                field_goals_made_19=(p_stats.get("made_19"),),
                field_goals_made_29=(p_stats.get("made_29"),),
                field_goals_made_39=(p_stats.get("made_39"),),
                field_goals_made_49=(p_stats.get("made_49"),),
                field_goals_made_50=(p_stats.get("made_50"),),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["extra_points_kicks"]) > 0:
        for p_stats in stat_list["extra_points_kicks"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                extra_points_kicks_attempts=(p_stats.get("attempts"),),
                extra_points_kicks_blocked=(p_stats.get("blocked"),),
                extra_points_kicks_made=(p_stats.get("made"),),
                extra_points_kicks_pct=(p_stats.get("pct"),),
            )
            all_game_stats.append(player_stats)

    if len(stat_list["extra_points_conversions"]) > 0:
        for p_stats in stat_list["extra_points_conversions"]:
            player_stats = PlayerGameStats(
                player_api_id=p_stats["id"],
                team_api_id=stat_list["team_api_id"],
                team_id=stat_list["team_id"],
                game_api_id=stat_list["game_api_id"],
                game_id=stat_list["game_id"],
                season_year=stat_list["game_season_year"],
                season_type=stat_list["game_season_type"],
                player_name=p_stats["name"],
                player_jersey=p_stats["jersey"],
                player_position=p_stats["position"],
                extra_points_conversions_pass_attempts=(p_stats.get("pass_attempts"),),
                extra_points_conversions_pass_successes=(
                    p_stats.get("pass_successes"),
                ),
                extra_points_conversions_rush_attempts=(p_stats.get("rush_attempts"),),
                extra_points_conversions_rush_successes=(
                    p_stats.get("rush_successes"),
                ),
                extra_points_conversions_defense_attempts=(
                    p_stats.get("defense_attempts"),
                ),
                extra_points_conversions_defense_successes=(
                    p_stats.get("defense_successes"),
                ),
                extra_points_conversions_turnover_successes=(
                    p_stats.get("turnover_successes"),
                ),
            )
            all_game_stats.append(player_stats)

    return all_game_stats


# Helps Organeze the game_stats_api return
def organize_player_game_stats(
    game_stats, game_api_id, general_game_db, isHome, season_year, season_type
):
    team_id = general_game_db.away_team_id
    team_id_api = general_game_db.away_team_api_id

    if isHome == True:
        team_id = general_game_db.home_team_id
        team_id_api = general_game_db.home_team_api_id

    players_stats_list = {
        "game_id": general_game_db.id,
        "game_api_id": game_api_id,
        "game_season_year": season_year,
        "game_season_type": season_type,
        "team_id": team_id,
        "team_api_id": team_id_api,
        "rushing": [],
        "receiving": [],
        "punts": [],
        "punt_returns": [],
        "penalties": [],
        "passing": [],
        "kickoffs": [],
        "kick_returns": [],
        "int_returns": [],
        "fumbles": [],
        "field_goals": [],
        "defense": [],
        "extra_points_kicks": [],
        "extra_points_conversions": [],
    }

    rushing_stats = game_stats.get("rushing")
    if rushing_stats and len(rushing_stats["players"]) > 0:
        players_stats_list["rushing"] = [player for player in rushing_stats["players"]]

    receiving_stats = game_stats.get("receiving")
    if receiving_stats and len(receiving_stats["players"]) > 0:
        players_stats_list["receiving"] = [
            player for player in receiving_stats["players"]
        ]

    punts_stats = game_stats.get("punts")
    if punts_stats and len(punts_stats["players"]) > 0:
        players_stats_list["punts"] = [player for player in punts_stats["players"]]

    punt_returns_stats = game_stats.get("punt_returns")
    if punt_returns_stats and len(punt_returns_stats["players"]) > 0:
        players_stats_list["punt_returns"] = [
            player for player in punt_returns_stats["players"]
        ]

    penalties_stats = game_stats.get("penalties")
    if penalties_stats and len(penalties_stats["players"]) > 0:
        players_stats_list["penalties"] = [
            player for player in penalties_stats["players"]
        ]

    passing_stats = game_stats.get("passing")
    if passing_stats and len(passing_stats["players"]) > 0:
        players_stats_list["passing"] = [player for player in passing_stats["players"]]

    kickoffs_stats = game_stats.get("kickoffs")
    if kickoffs_stats and len(kickoffs_stats["players"]) > 0:
        players_stats_list["kickoffs"] = [
            player for player in kickoffs_stats["players"]
        ]

    kick_returns_stats = game_stats.get("kick_returns")
    if kick_returns_stats and len(kick_returns_stats["players"]) > 0:
        players_stats_list["kick_returns"] = [
            player for player in kick_returns_stats["players"]
        ]

    int_returns_stats = game_stats.get("int_returns")
    if int_returns_stats and len(int_returns_stats["players"]) > 0:
        players_stats_list["int_returns"] = [
            player for player in int_returns_stats["players"]
        ]

    fumbles_stats = game_stats.get("fumbles")
    if fumbles_stats and len(fumbles_stats["players"]) > 0:
        players_stats_list["fumbles"] = [player for player in fumbles_stats["players"]]

    field_goals_stats = game_stats.get("field_goals")
    if field_goals_stats and len(field_goals_stats["players"]) > 0:
        players_stats_list["field_goals"] = [
            player for player in field_goals_stats["players"]
        ]

    defense_stats = game_stats.get("defense")
    if defense_stats and len(defense_stats["players"]) > 0:
        players_stats_list["defense"] = [player for player in defense_stats["players"]]

    extra_points_kicks = game_stats.get("extra_points")["kicks"]
    if extra_points_kicks and len(extra_points_kicks["players"]) > 0:
        players_stats_list["extra_points_kicks"] = [
            player for player in extra_points_kicks["players"]
        ]

    extra_points_conversions = game_stats.get("extra_points")["conversions"]
    if extra_points_conversions and len(extra_points_conversions["players"]) > 0:
        players_stats_list["extra_points_conversions"] = [
            player for player in extra_points_conversions["players"]
        ]

    return players_stats_list
