from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
import uuid

from database import get_db, Base, engine
from models import Book
from schema import BookCreate, BookResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "I keep dancing on my own!"}

@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    books = db.scalars(select(Book)).all()
    return books

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: uuid.UUID, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

@app.post("/books", response_model=BookResponse)
def post_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
