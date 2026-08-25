import pytest
from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from models import Book, GenreEnum
from database import Base
from main import app, get_db

TEST_DB_URL = "sqlite:///:memory:"
test_engine = create_engine(
            url=TEST_DB_URL,
            echo=True,
            poolclass=StaticPool,
            connect_args={"check_same_thread": False}
            )

TestSessionLocal = sessionmaker(bind=test_engine, autocommit=False, autoflush=False)

@pytest.fixture(scope="session")
def setup_db():
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture
def db_session(setup_db):
    test_db_session = TestSessionLocal()
    yield test_db_session
    test_db_session.query(Book).delete()
    test_db_session.commit()
    test_db_session.close()

@pytest.fixture
def client(db_session):
    def _override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = _override_get_db
    test_client = TestClient(app)
    yield test_client
    app.dependency_overrides.clear()

@pytest.fixture
def sample_book(db_session):
    new_book = Book(
                title="Turtles All The Way Down",
                author="John Green",
                published_year=2017,
                genre=GenreEnum.FICTION,
            )
    db_session.add(new_book)
    db_session.commit()
    db_session.refresh(new_book)
    yield new_book













