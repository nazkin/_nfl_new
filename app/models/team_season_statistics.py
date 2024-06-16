from sqlalchemy import Column
from sqlalchemy import Integer, Boolean, Float
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TeamSeasonStats(Base):

    __tablename__ = "team_season_stats"
    id = Column("id", Integer(), primary_key=True, autoincrement=True)
    team_id = Column("team_id", Integer)
    team_api_id = Column("team_api_id", String(225))
    season_year = Column("season_year", Integer())
    season_type = Column("season_type", String())
    is_opponent_stats = Column("is_opponent_stats", Boolean())
    games_played = Column("games_played", Integer())
    touchdown_passes = Column("touchdown_passes", Integer())
    touchdown_rushes = Column("touchdown_rushes", Integer())
    touchdown_total_return = Column("touchdown_total_return", Integer())
    touchdown_total = Column("touchdown_total", Integer())
    touchdown_fumble_return = Column("touchdown_fumble_return", Integer())
    touchdown_point_return = Column("touchdown_point_return", Integer())
    touchdown_int_return = Column("touchdown_int_return", Integer())
    touchdown_kick_return = Column("touchdown_kick_return", Integer())
    touchdown_point_return = Column("touchdown_point_return", Integer())
    touchdown_other = Column("touchdown_other", Integer())
    rushing_avg_yards = Column("rushing_avg_yards", Integer())
    rushing_attempts = Column("rushing_attempts", Integer())
    rushing_touchdowns = Column("rushing_touchdowns", Integer())
    rushing_tlost = Column("rushing_tlost", Integer())
    rushing_tlost_yards = Column("rushing_tlost_yards", Integer())
    rushing_yards = Column("rushing_yards", Integer())
    rushing_longest = Column("rushing_longest", Integer())
    rushing_longest_touchdown = Column("rushing_longest_touchdown", Integer())
    rushing_redzone_attempts = Column("rushing_redzone_attempts", Integer())
    rushing_brocken_tackles = Column("rushing_brocken_tackles", Integer())
    rushing_kneel_downs = Column("rushing_kneel_downs", Integer())
    rushing_scrambles = Column("rushing_scrambles", Integer())
    rushing_yards_after_contact = Column("rushing_yards_after_contact", Integer())
    receiving_targets = Column("receiving_targets", Integer())
    receiving_receptions = Column("receiving_receptions", Integer())
    receiving_avg_yards = Column("receiving_avg_yards", Float())
    receiving_yards = Column("receiving_yards", Integer())
    receiving_touchdowns = Column("receiving_touchdowns", Integer())
    receiving_yards_after_catch = Column("receiving_yards_after_catch", Integer())
    receiving_longest = Column("receiving_longest", Integer())
    receiving_longest_touchdown = Column("receiving_longest_touchdown", Integer())
    receiving_redzone_targets = Column("receiving_redzone_targets", Integer())
    receiving_air_yards = Column("receiving_air_yards", Integer())
    receiving_broken_tackles = Column("receiving_broken_tackles", Integer())
    receiving_dropped_passes = Column("receiving_dropped_passes", Integer())
    receiving_catchable_passes = Column("receiving_catchable_passes", Integer())
    receiving_yards_after_contact = Column("receiving_yards_after_contact", Integer())
    punts_attempts = Column("punts_attempts", Integer())
    punts_yards = Column("punts_yards", Integer())
    punts_net_yards = Column("punts_net_yards", Integer())
    punts_blocked = Column("punts_blocked", Integer())
    punts_touchbacks = Column("punts_touchbacks", Integer())
    punts_inside_20 = Column("punts_inside_20", Integer())
    punts_return_yards = Column("punts_return_yards", Float())
    punts_avg_net_yards = Column("punts_avg_net_yards", Float())
    punts_avg_yards = Column("punts_avg_yards", Float())
    punts_longest = Column("punts_longest", Integer())
    punts_hang_time = Column("punts_hang_time", Float())
    punts_avg_hang_time = Column("punts_avg_hang_time", Float())
    punt_returns_avg_yards = Column("punt_returns_avg_yards", Float())
    punt_returns_yards = Column("punt_returns_yards", Integer())
    punt_returns_longest = Column("punt_returns_longest", Integer())
    punt_returns_touchdowns = Column("punt_returns_touchdowns", Integer())
    punt_returns_longest_touchdown = Column("punt_returns_longest_touchdown", Integer())
    punt_returns_faircatches = Column("punt_returns_faircatches", Integer())
    penalties_penalties = Column("penalties_penalties", Integer())
    penalties_yards = Column("penalties_yards", Integer())
    passing_attempts = Column("passing_attempts", Integer())
    passing_completions = Column("passing_completions", Integer())
    passing_cmp_pct = Column("passing_cmp_pct", Float())
    passing_interceptions = Column("passing_interceptions", Integer())
    passing_sack_yards = Column("passing_sack_yards", Integer())
    passing_rating = Column("passing_rating", Integer())
    passing_touchdowns = Column("passing_touchdowns", Integer())
    passing_avg_yards = Column("passing_avg_yards", Float())
    passing_sacks = Column("passing_sacks", Integer())
    passing_longest = Column("passing_longest", Integer())
    passing_longest_touchdown = Column("passing_longest_touchdown", Integer())
    passing_air_yards = Column("passing_air_yards", Integer())
    passing_redzone_attempts = Column("passing_redzone_attempts", Integer())
    passing_net_yards = Column("passing_net_yards", Integer())
    passing_yards = Column("passing_yards", Integer())
    passing_gross_yards = Column("passing_gross_yards", Integer())
    passing_int_touchdowns = Column("passing_int_touchdowns", Integer())
    passing_throw_aways = Column("passing_throw_aways", Integer())
    passing_poor_throws = Column("passing_poor_throws", Integer())
    passing_defended_passes = Column("passing_defended_passes", Integer())
    passing_dropped_passes = Column("passing_dropped_passes", Integer())
    passing_spikes = Column("passing_spikes", Integer())
    passing_blitzes = Column("passing_blitzes", Integer())
    passing_hurries = Column("passing_hurries", Integer())
    passing_knockdowns = Column("passing_knockdowns", Integer())
    passing_pocket_time = Column("passing_pocket_time", Float())
    passing_batted_passes = Column("passing_batted_passes", Integer())
    passing_on_target_throws = Column("passing_on_target_throws", Integer())
    kickoffs_endzone = Column("kickoffs_endzone", Integer())
    kickoffs_inside_20 = Column("kickoffs_inside_20", Integer())
    kickoffs_return_yards = Column("kickoffs_return_yards", Integer())
    kickoffs_returned = Column("kickoffs_returned", Integer())
    kickoffs_touchbacks = Column("kickoffs_touchbacks", Integer())
    kickoffs_yards = Column("kickoffs_yards", Integer())
    kickoffs_out_of_bounds = Column("kickoffs_out_of_bounds", Integer())
    kickoffs_kickoffs = Column("kickoffs_kickoffs", Integer())
    kickoffs_onside_successes = Column("kickoffs_onside_successes", Integer())
    kickoffs_onside_attempts = Column("kickoffs_onside_attempts", Integer())
    kickoffs_squib_kicks = Column("kickoffs_squib_kicks", Integer())
    kick_returns_avg_yards = Column("kick_returns_avg_yards", Integer())
    kick_returns_yards = Column("kick_returns_yards", Integer())
    kick_returns_longest = Column("kick_returns_longest", Integer())
    kick_returns_touchdowns = Column("kick_returns_touchdowns", Integer())
    kick_returns_longest_touchdown = Column("kick_returns_longest_touchdown", Integer())
    kick_returns_faircatches = Column("kick_returns_faircatches", Integer())
    kick_returns_returns = Column("kick_returns_returns", Integer())
    interceptions_return_yards = Column("interceptions_return_yards", Integer())
    interceptions_returned = Column("interceptions_returned", Integer())
    interceptions_interceptions = Column("interceptions_interceptions", Integer())
    int_returns_avg_yards = Column("int_returns_avg_yards", Float())
    int_returns_yards = Column("int_returns_yards", Integer())
    int_returns_longest = Column("int_returns_longest", Integer())
    int_returns_touchdowns = Column("int_returns_touchdowns", Integer())
    int_returns_longest_touchdown = Column("int_returns_longest_touchdown", Integer())
    int_returns_returns = Column("int_returns_returns", Integer())
    fumbles_fumbles = Column("fumbles_fumbles", Integer())
    fumbles_lost_fumbles = Column("fumbles_lost_fumbles", Integer())
    fumbles_own_rec = Column("fumbles_own_rec", Integer())
    fumbles_own_rec_yards = Column("fumbles_own_rec_yards", Integer())
    fumbles_opp_rec = Column("fumbles_opp_rec", Integer())
    fumbles_out_of_bounds = Column("fumbles_out_of_bounds", Integer())
    fumbles_forced_fumbles = Column("fumbles_forced_fumbles", Integer())
    fumbles_own_rec_tds = Column("fumbles_own_rec_tds", Integer())
    fumbles_opp_rec_tds = Column("fumbles_opp_rec_tds", Integer())
    fumbles_ez_rec_tds = Column("fumbles_ez_rec_tds", Integer())
    first_downs_pass = Column("first_downs_pass", Integer())
    first_downs_penalty = Column("first_downs_penalty", Integer())
    first_downs_rush = Column("first_downs_rush", Integer())
    first_downs_total = Column("first_downs_total", Integer())
    field_goals_attempts = Column("field_goals_attempts", Integer())
    field_goals_made = Column("field_goals_made", Integer())
    field_goals_blocked = Column("field_goals_blocked", Integer())
    field_goals_yards = Column("field_goals_yards", Integer())
    field_goals_avg_yards = Column("field_goals_avg_yards", Float())
    field_goals_longest = Column("field_goals_longest", Integer())
    field_goals_missed = Column("field_goals_missed", Integer())
    field_goals_pct = Column("field_goals_pct", Float())
    field_goals_attempts_19 = Column("field_goals_attempts_19", Integer())
    field_goals_attempts_29 = Column("field_goals_attempts_29", Integer())
    field_goals_attempts_39 = Column("field_goals_attempts_39", Integer())
    field_goals_attempts_49 = Column("field_goals_attempts_49", Integer())
    field_goals_attempts_50 = Column("field_goals_attempts_50", Integer())
    field_goals_made_19 = Column("field_goals_made_19", Integer())
    field_goals_made_29 = Column("field_goals_made_29", Integer())
    field_goals_made_39 = Column("field_goals_made_39", Integer())
    field_goals_made_49 = Column("field_goals_made_49", Integer())
    field_goals_made_50 = Column("field_goals_made_50", Integer())
    defence_tackles = Column("defence_tackles", Integer())
    defence_assists = Column("defence_assists", Integer())
    defence_combined = Column("defence_combined", Integer())
    defence_sacks = Column("defence_sacks", Integer())
    defence_sack_yards = Column("defence_sack_yards", Integer())
    defence_interceptions = Column("defence_interceptions", Integer())
    defence_passes_defended = Column("defence_passes_defended", Integer())
    defence_forced_fumbles = Column("defence_forced_fumbles", Integer())
    defence_fumble_recoveries = Column("defence_fumble_recoveries", Integer())
    defence_qb_hits = Column("defence_qb_hits", Integer())
    defence_tloss = Column("defence_tloss", Integer())
    defence_tloss_yards = Column("defence_tloss_yards", Integer())
    defence_safeties = Column("defence_safeties", Integer())
    defence_sp_tackles = Column("defence_sp_tackles", Integer())
    defence_sp_assists = Column("defence_sp_assists", Integer())
    defence_sp_forced_fumbles = Column("defence_sp_forced_fumbles", Integer())
    defence_sp_fumble_recoveries = Column("defence_sp_fumble_recoveries", Integer())
    defence_sp_blocks = Column("defence_sp_blocks", Integer())
    defence_misc_tackles = Column("defence_misc_tackles", Integer())
    defence_misc_assists = Column("defence_misc_assists", Integer())
    defence_misc_forced_fumbles = Column("defence_misc_forced_fumbles", Integer())
    defence_misc_fumble_recoveries = Column("defence_misc_fumble_recoveries", Integer())
    defence_def_targets = Column("defence_def_targets", Integer())
    defence_def_comps = Column("defence_def_comps", Integer())
    defence_blitzes = Column("defence_blitzes", Integer())
    defence_hurries = Column("defence_hurries", Integer())
    defence_knockdowns = Column("defence_knockdowns", Integer())
    defence_missed_tackles = Column("defence_missed_tackles", Integer())
    defence_batted_passes = Column("defence_batted_passes", Integer())
    defence_three_and_outs_forced = Column("defence_three_and_outs_forced", Integer())
    defence_fourth_down_stops = Column("defence_fourth_down_stops", Integer())
    extra_points_kicks_attempts = Column("extra_points_kicks_attempts", Integer())
    extra_points_kicks_blocked = Column("extra_points_kicks_blocked", Integer())
    extra_points_kicks_made = Column("extra_points_kicks_made", Integer())
    extra_points_kicks_pct = Column("extra_points_kicks_pct", Float())
    extra_points_conversions_pass_attempts = Column(
        "extra_points_conversions_pass_attempts", Integer()
    )
    extra_points_conversions_pass_successes = Column(
        "extra_points_conversions_pass_successes", Integer()
    )
    extra_points_conversions_rush_attempts = Column(
        "extra_points_conversions_rush_attempts", Integer()
    )
    extra_points_conversions_rush_successes = Column(
        "extra_points_conversions_rush_successes", Integer()
    )
    extra_points_conversions_defense_attempts = Column(
        "extra_points_conversions_defense_attempts", Integer()
    )
    extra_points_conversions_defense_successes = Column(
        "extra_points_conversions_defense_successes", Integer()
    )
    extra_points_conversions_turnover_successes = Column(
        "extra_points_conversions_turnover_successes", Integer()
    )
    efficiency_goaltogo_attempts = Column("efficiency_goaltogo_attempts", Integer())
    efficiency_goaltogo_successes = Column("efficiency_goaltogo_successes", Integer())
    efficiency_goaltogo_pct = Column("efficiency_goaltogo_pct", Float())
    efficiency_redzone_attempts = Column("efficiency_redzone_attempts", Integer())
    efficiency_redzone_successes = Column("efficiency_redzone_successes", Integer())
    efficiency_redzone_pct = Column("efficiency_redzone_pct", Float())
    efficiency_thirddown_attempts = Column("efficiency_thirddown_attempts", Integer())
    efficiency_thirddown_successes = Column("efficiency_thirddown_successes", Integer())
    efficiency_thirddown_pct = Column("efficiency_thirddown_pct", Float())
    efficiency_fourthdown_attempts = Column("efficiency_fourthdown_attempts", Integer())
    efficiency_fourthdown_successes = Column(
        "efficiency_fourthdown_successes", Integer()
    )
    efficiency_fourthdown_pct = Column("efficiency_fourthdown_pct", Float())
