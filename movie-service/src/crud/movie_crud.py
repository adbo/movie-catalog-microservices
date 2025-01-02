from sqlmodel import Session, select
from typing import List
from sqlalchemy import or_

from ..models.movie import Movie

def search_movies(db: Session, query: str) -> List[Movie]:
    statement = select(Movie).where(
        (Movie.title.ilike(f"%{query}%")) | (Movie.description.ilike(f"%{query}%"))
    )
    results = db.exec(statement)
    return results.all()