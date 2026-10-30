import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_existing_post():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"] != ""


def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/999999")

    assert response.status_code == 404