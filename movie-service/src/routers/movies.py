from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session

from ..crud import movie_crud
from ..database.database import get_db
from ..models.movie import Movie


router = APIRouter()

@router.get("/movies/search", response_model=List[Movie])
def search_movies(q: str, db: Session = Depends(get_db)):
    return movie_crud.search_movies(db, query=q)