from fastapi import FastAPI
from app.routes.team_and_players_general import router as team_and_player_general_routes
from app.routes.seasons import router as seasons_routes
from app.routes.team_season_stats import router as team_season_stats_router
from dotenv import load_dotenv
from app.db_context import get_db

app = FastAPI()



load_dotenv()
get_db()
app.include_router(team_and_player_general_routes)
app.include_router(seasons_routes)
app.include_router(team_season_stats_router)