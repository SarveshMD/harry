from models import Book
from database import Base, engine

Base.metadata.create_all(bind=engine)
