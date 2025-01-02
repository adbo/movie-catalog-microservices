from fastapi import FastAPI
from .routers import movies
from sqlmodel import SQLModel, create_engine
from .settings import Settings

settings = Settings()
engine = create_engine(settings.database_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI(on_startup=[create_db_and_tables])

app.include_router(movies.router)