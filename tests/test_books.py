from fastapi import status

def test_home(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "I keep dancing on my own!"}

def test_get_books_empty(client):
    response = client.get("/books")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

def test_get_books_sample(client, sample_book):
    response = client.get("/books")
    assert response.status_code == status.HTTP_200_OK
    res_book = response.json()[0]
    assert res_book['title'] == "Turtles All The Way Down"
    assert res_book['author'] == "John Green"
    assert res_book['published_year'] == 2017
    assert res_book['genre'] == "fiction"
    assert res_book['is_available'] == True
