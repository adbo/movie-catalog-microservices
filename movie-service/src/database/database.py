from sqlmodel import create_engine, Session
from ..settings import Settings

settings = Settings()

engine = create_engine(settings.database_url)

def get_db():
    with Session(engine) as session:
        yield session