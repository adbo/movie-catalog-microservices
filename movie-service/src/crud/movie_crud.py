from sqlmodel import Session, select
from typing import List
from sqlalchemy import func

from ..models.movie import Movie, MovieCreate

def search_movies(db: Session, query: str) -> List[Movie]:
    statement = select(Movie).where(
        (Movie.title.ilike(f"%{query}%")) | 
        (Movie.description.ilike(f"%{query}%")) |
        (func.array_to_string(Movie.actors, ', ').ilike(f"%{query}%"))
    )
    results = db.exec(statement)
    return results.all()

def create_movie(db: Session, movie: MovieCreate) -> Movie:
    db_movie = Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie