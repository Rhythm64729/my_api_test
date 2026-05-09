import requests


def test_get_user_info():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert data["id"] == 1


def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    new_data = {
        "title": "test title",
        "body": "test body",
        "userId": 99
    }
    response = requests.post(url, json=new_data)

    assert response.status_code == 201
    result = response.json()
    assert result["title"] == "test title"