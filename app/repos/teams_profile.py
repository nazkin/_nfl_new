from typing import List

from app.models.teams_profile import TeamsProfile
from app.db_context import sessionmaker


async def insert_team_profile(team: TeamsProfile):
    id = None
    with sessionmaker.begin() as session:
        session.expire_on_commit = False
        try:
            session.add(team)

            session.flush()
            id = team.id
            session.commit()
        except Exception as ex:
            print(f"Exception storing team {team.name}: {ex}")

    return id


def fetch_all_teams():
    with sessionmaker.begin() as session:
        session.expire_on_commit = False
        return session.query(TeamsProfile).where(TeamsProfile.id > 0).all()
