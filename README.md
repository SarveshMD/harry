# harry

harry is a practice repo.

## How to run

1. Set up a PostgreSQL database.

2. Create a .env file and add the database URL:

```shell
DATABASE_URL="postgresql+psycopg://<username>:<password>@<host>:<port>/<db_name>"
```

3. Create and activate a virtual environment:

```shell
python3 -m venv env
source env/bin/activate
```

4. Install Dependencies:

```shell
pip install -r requirements.txt
```

5. Initialize the Database:

```shell
python3 init_db.py
```

6. Run the app

```shell
uvicorn main:app --reload
```

## How to test

```shell
pytest tests
```

## Tech Stack

    - FastAPI
    - PostgreSQL
    - SQLAlchemy
    - Pydantic
    - Pytest

## CRUD: Book Resource

Structure of a Book entity

```python
class Book:
    id: uuid.UUID
    title: str
    author: str
    description: str | None
    published_year: int
    genre: GenreEnum
    is_available: bool = True

class GenreEnum(str, enum.Enum):
    FICTION = 'fiction'
    NONFICTION = 'nonfiction'
    ROMANCE = 'romance'
    SCIFI = 'scifi'
    FANTASY = 'fantasy'
```

## Routes

| Method   | Endpoint           | Description             | Success Status   |
| -------- | ------------------ | ----------------------- | ---------------- |
| `GET`    | `/books`           | Get all books           | `200 OK`         |
| `GET`    | `/books/{book_id}` | Get a book by UUID      | `200 OK`         |
| `POST`   | `/books`           | Create a book           | `201 Created`    |
| `PUT`    | `/books/{book_id}` | Replace a book          | `200 OK`         |
| `PATCH`  | `/books/{book_id}` | Partially update a book | `200 OK`         |
| `DELETE` | `/books/{book_id}` | Delete a book           | `204 No Content` |
