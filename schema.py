from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime

from models import GenreEnum


class BookBase(BaseModel):
    title: str
    author: str
    description: str | None = None
    published_year: int
    genre: GenreEnum
    is_available: bool = True


class BookCreate(BookBase):
    model_config = ConfigDict(extra='forbid')


class BookResponse(BookBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    created_at: datetime


class BookPatch(BaseModel):
    model_config = ConfigDict(extra='forbid')

    title: str | None = None
    author: str | None = None
    description: str | None = None
    published_year: int | None = None
    genre: GenreEnum | None = None
    is_available: bool | None = None
