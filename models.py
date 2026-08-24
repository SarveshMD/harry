from database import Base

from datetime import datetime, timezone
import uuid
import enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Enum, UUID, Boolean, DateTime

class GenreEnum(str, enum.Enum):
    FICTION = 'fiction'
    NONFICTION = 'nonfiction'
    ROMANCE = 'romance'
    SCIFI = 'scifi'
    FANTASY = 'fantasy'

class Book(Base):
    __tablename__ = 'books'

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(4000))
    published_year: Mapped[int] = mapped_column(Integer)
    genre: Mapped[GenreEnum] = mapped_column(Enum(GenreEnum), name='genre_enum')
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, title={self.title!r}, \
                author={self.author!r}, description={self.description!r}, \
                published_year={self.published_year!r}, genre={self.genre!r}, \
                is_available={self.is_available!r}, created_at={self.created_at!r})"
