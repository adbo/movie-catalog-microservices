from fastapi import APIRouter
from typing import List

from ..models.movie import Movie

router = APIRouter()


@router.get("/movies/search", response_model=List[Movie])
def search_movies(q: str):
    pass