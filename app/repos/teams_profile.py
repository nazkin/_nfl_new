from app.models.teams_profile import TeamsProfile
from app.db_context import sessionmaker


def insert_team_profile(team: TeamsProfile):
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


def fetch_team_from_db_by_api_id(api_id: str) -> TeamsProfile:
    with sessionmaker.begin() as session:
        session.expire_on_commit = False
        return (
            session.query(TeamsProfile)
            .where(TeamsProfile.team_api_id == api_id)
            .first()
        )
