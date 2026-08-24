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

@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def post_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: uuid.UUID, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return None

@app.put("/books/{book_id}", response_model=BookResponse)
def put_book(book_id: uuid.UUID, book: BookCreate, db: Session = Depends(get_db)):
    old_book = db.get(Book, book_id)
    if old_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    old_book.title = book.title
    old_book.author = book.author
    old_book.description = book.description
    old_book.published_year = book.published_year
    old_book.genre = book.genre
    old_book.is_available = book.is_available

    db.commit()
    db.refresh(old_book)
    return old_book
