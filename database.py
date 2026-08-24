from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

from config import settings

class Base(DeclarativeBase):
    pass

engine = create_engine(url=settings.database_url, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
