from sqlmodel import Session, select
from typing import List
from sqlalchemy import func

from ..models.movie import Movie

def search_movies(db: Session, query: str) -> List[Movie]:
    statement = select(Movie).where(
        (Movie.title.ilike(f"%{query}%")) | 
        (Movie.description.ilike(f"%{query}%")) |
        (func.array_to_string(Movie.actors, ', ').ilike(f"%{query}%"))
    )
    results = db.exec(statement)
    return results.all()