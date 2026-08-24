from pydantic import BaseModel
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
    pass

class BookResponse(BookBase):
    id: uuid.UUID
    created_at: datetime
