from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class PlayerGameStats(Base):
    __tablename__ = "player_game_stats"
    id = Column(Integer, primary_key=True)
    player_api_id = Column(String(200))
    player_id = Column(Integer)
    team_api_id = Column(String(200))
    team_id = Column(Integer)
    game_api_id = Column(String(200))
    game_id = Column(Integer)
    player_name = Column(String())
    player_jersey = Column(String())
    player_position = Column(String())
    season_year = Column(Integer())
    season_type = Column(String())
    rushing_avg_yards = Column(Float)
    rushing_attempts = Column(Integer)
    rushing_touchdowns = Column(Integer)
    rushing_tlost = Column(Integer)
    rushing_tlost_yards = Column(Integer)
    rushing_yards = Column(Integer)
    rushing_longest = Column(Integer)
    rushing_longest_touchdown = Column(Integer)
    rushing_redzone_attempts = Column(Integer)
    rushing_broken_tackles = Column(Integer)
    rushing_kneel_downs = Column(Integer)
    rushing_scrambles = Column(Integer)
    rushing_yards_after_contact = Column(Integer)
    rushing_first_down = Column(Integer)
    receiving_targets = Column(Integer)
    receiving_receptions = Column(Integer)
    receiving_avg_yards = Column(Float)
    receiving_yards = Column(Integer)
    receiving_touchdowns = Column(Integer)
    receiving_yards_after_catch = Column(Integer)
    receiving_longest = Column(Integer)
    receiving_longest_touchdown = Column(Integer)
    receiving_redzone_targets = Column(Integer)
    receiving_air_yards = Column(Integer)
    receiving_broken_tackles = Column(Integer)
    receiving_dropped_passes = Column(Integer)
    receiving_catchable_passes = Column(Integer)
    receiving_yards_after_contact = Column(Integer)
    receiving_first_downs = Column(Integer)
    punts_attempts = Column(Integer)
    punts_yards = Column(Integer)
    punts_net_yards = Column(Integer)
    punts_blocked = Column(Integer)
    punts_touchbacks = Column(Integer)
    punts_inside_20 = Column(Integer)
    punts_return_yards = Column(Float)
    punts_avg_net_yards = Column(Float)
    punts_avg_yards = Column(Float)
    punts_longest = Column(Integer)
    punts_hang_time = Column(Float)
    punts_avg_hang_time = Column(Float)
    punt_returns_avg_yards = Column(Float)
    punt_returns_yards = Column(Integer)
    punt_returns_longest = Column(Integer)
    punt_returns_touchdowns = Column(Integer)
    punt_returns_longest_touchdown = Column(Integer)
    punt_returns_faircatches = Column(Integer)
    punt_returns_number = Column(Integer)
    penalties_penalties = Column(Integer)
    penalties_yards = Column(Integer)
    penalties_first_downs = Column(Integer)
    passing_attempts = Column(Integer)
    passing_completions = Column(Integer)
    passing_cmp_pct = Column(Float)
    passing_interceptions = Column(Integer)
    passing_sack_yards = Column(Integer)
    passing_rating = Column(Integer)
    passing_touchdowns = Column(Integer)
    passing_avg_yards = Column(Float)
    passing_sacks = Column(Integer)
    passing_longest = Column(Integer)
    passing_longest_touchdown = Column(Integer)
    passing_air_yards = Column(Integer)
    passing_redzone_attempts = Column(Integer)
    passing_net_yards = Column(Integer)
    passing_yards = Column(Integer)
    passing_gross_yards = Column(Integer)
    passing_int_touchdowns = Column(Integer)
    passing_throw_aways = Column(Integer)
    passing_poor_throws = Column(Integer)
    passing_defended_passes = Column(Integer)
    passing_dropped_passes = Column(Integer)
    passing_spikes = Column(Integer)
    passing_blitzes = Column(Integer)
    passing_hurries = Column(Integer)
    passing_knockdowns = Column(Integer)
    passing_pocket_time = Column(Float)
    passing_batted_passes = Column(Integer)
    passing_on_target_throws = Column(Integer)
    passing_first_downs = Column(Integer)
    kickoffs_endzone = Column(Integer)
    kickoffs_total_endzone = Column(Integer)
    kickoffs_inside_20 = Column(Integer)
    kickoffs_return_yards = Column(Integer)
    kickoffs_number = Column(Integer)
    kickoffs_touchbacks = Column(Integer)
    kickoffs_yards = Column(Integer)
    kickoffs_out_of_bounds = Column(Integer)
    kickoffs_kickoffs = Column(Integer)
    kickoffs_onside_successes = Column(Integer)
    kickoffs_onside_attempts = Column(Integer)
    kickoffs_squib_kicks = Column(Integer)
    kick_returns_avg_yards = Column(Integer)
    kick_returns_yards = Column(Integer)
    kick_returns_longest = Column(Integer)
    kick_returns_touchdowns = Column(Integer)
    kick_returns_longest_touchdown = Column(Integer)
    kick_returns_faircatches = Column(Integer)
    kick_returns_number = Column(Integer)
    int_returns_avg_yards = Column(Float)
    int_returns_yards = Column(Integer)
    int_returns_longest = Column(Integer)
    int_returns_touchdowns = Column(Integer)
    int_returns_longest_touchdown = Column(Integer)
    int_returns_number = Column(Integer)
    fumbles_fumbles = Column(Integer)
    fumbles_lost_fumbles = Column(Integer)
    fumbles_own_rec = Column(Integer)
    fumbles_own_rec_yards = Column(Integer)
    fumbles_opp_rec = Column(Integer)
    fumbles_out_of_bounds = Column(Integer)
    fumbles_forced_fumbles = Column(Integer)
    fumbles_own_rec_tds = Column(Integer)
    fumbles_opp_rec_tds = Column(Integer)
    fumbles_ez_rec_tds = Column(Integer)
    field_goals_attempts = Column(Integer)
    field_goals_made = Column(Integer)
    field_goals_blocked = Column(Integer)
    field_goals_yards = Column(Integer)
    field_goals_avg_yards = Column(Float)
    field_goals_longest = Column(Integer)
    field_goals_missed = Column(Integer)
    field_goals_pct = Column(Float)
    field_goals_attempts_19 = Column(Integer)
    field_goals_attempts_29 = Column(Integer)
    field_goals_attempts_39 = Column(Integer)
    field_goals_attempts_49 = Column(Integer)
    field_goals_attempts_50 = Column(Integer)
    field_goals_made_19 = Column(Integer)
    field_goals_made_29 = Column(Integer)
    field_goals_made_39 = Column(Integer)
    field_goals_made_49 = Column(Integer)
    field_goals_made_50 = Column(Integer)
    defence_tackles = Column(Integer)
    defence_assists = Column(Integer)
    defence_combined = Column(Integer)
    defence_sacks = Column(Integer)
    defence_sack_yards = Column(Integer)
    defence_interceptions = Column(Integer)
    defence_passes_defended = Column(Integer)
    defence_forced_fumbles = Column(Integer)
    defence_fumble_recoveries = Column(Integer)
    defence_qb_hits = Column(Integer)
    defence_tloss = Column(Integer)
    defence_tloss_yards = Column(Integer)
    defence_safeties = Column(Integer)
    defence_sp_tackles = Column(Integer)
    defence_sp_assists = Column(Integer)
    defence_sp_forced_fumbles = Column(Integer)
    defence_sp_fumble_recoveries = Column(Integer)
    defence_sp_blocks = Column(Integer)
    defence_misc_tackles = Column(Integer)
    defence_misc_assists = Column(Integer)
    defence_misc_forced_fumbles = Column(Integer)
    defence_misc_fumble_recoveries = Column(Integer)
    defence_def_targets = Column(Integer)
    defence_def_comps = Column(Integer)
    defence_blitzes = Column(Integer)
    defence_hurries = Column(Integer)
    defence_knockdowns = Column(Integer)
    defence_missed_tackles = Column(Integer)
    defence_batted_passes = Column(Integer)
    defence_three_and_outs_forced = Column(Integer)
    defence_fourth_down_stops = Column(Integer)
    extra_points_kicks_attempts = Column(Integer)
    extra_points_kicks_blocked = Column(Integer)
    extra_points_kicks_made = Column(Integer)
    extra_points_kicks_pct = Column(Float)
    extra_points_conversions_pass_attempts = Column(Integer)
    extra_points_conversions_pass_successes = Column(Integer)
    extra_points_conversions_rush_attempts = Column(Integer)
    extra_points_conversions_rush_successes = Column(Integer)
    extra_points_conversions_defense_attempts = Column(Integer)
    extra_points_conversions_defense_successes = Column(Integer)
    extra_points_conversions_turnover_successes = Column(Integer)