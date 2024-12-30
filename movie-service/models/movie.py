from typing import Optional, List
from sqlmodel import SQLModel, Field


class MovieBase(SQLModel):
    title: str
    description: Optional[str] = None
    genre: str
    director: str
    actors: List[str] = []

class Movie(MovieBase):
    id: Optional[int] = Field(default=None, primary_key=True)