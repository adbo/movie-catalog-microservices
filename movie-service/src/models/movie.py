from typing import Optional, List
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.sql.sqltypes import Unicode



class MovieBase(SQLModel):
    title: str
    description: Optional[str] = None
    genre: str
    director: str
    actors: List[str] = Field(sa_column=Column(ARRAY(Unicode)))

class Movie(MovieBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class MovieCreate(MovieBase):
    pass

class MovieUpdate(MovieBase):
    title: Optional[str] = None
    description: Optional[str] = None
    genre: Optional[str] = None
    director: Optional[str] = None
    actors: Optional[List[str]] = []