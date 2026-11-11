import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_existing_post():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"] != ""
    assert isinstance(data["title"], str)
    assert data["title"].strip() != ""

def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/999999", timeout=10)

    assert response.status_code == 404


def test_get_posts_by_user():
    response = requests.get(
        f"{BASE_URL}/posts",
        params={"userId": 1},
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for post in data:
        assert post["userId"] == 1


def test_create_post():
    payload = {
        "title": "QA Automation Portfolio",
        "body": "Learning API testing with Python and Requests",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data