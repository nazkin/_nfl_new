from fastapi import FastAPI
from app.routes.team_and_players_general import router as team_and_player_general_routes
from app.routes.seasons import router as seasons_routes
from app.routes.team_season_stats import router as team_season_stats_router
from app.routes.player_season_stats import router as player_season_stats_router
from app.routes.games import router as season_games_router
from app.routes.team_game_stats import router as team_game_stats_router
from app.routes.player_game_stats import router as player_game_stats_router
from dotenv import load_dotenv
from app.db_context import get_db

app = FastAPI()

load_dotenv()

get_db()

app.include_router(seasons_routes)
app.include_router(team_and_player_general_routes)
app.include_router(team_season_stats_router)
app.include_router(player_season_stats_router)
app.include_router(season_games_router)
app.include_router(team_game_stats_router)
app.include_router(player_game_stats_router)
