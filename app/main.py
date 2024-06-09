from fastapi import FastAPI
from app.routes.general_fill_out import router as general_fill_out_router
from dotenv import load_dotenv
from app.db_context import get_db

app = FastAPI()



load_dotenv()
get_db()
app.include_router(general_fill_out_router)