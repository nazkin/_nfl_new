import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = "postgresql://postgres:19935ert7@localhost/football"
engine = create_engine(database_url)
sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = sessionmaker()
    print(f"COnnecting to db {database_url}")
    try:
        print("Yield")
        yield db
    finally:
        print("Fail")
        db.close()


API_KEY = os.getenv("API_KEY")
