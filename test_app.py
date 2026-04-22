import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Hello, CI/CD!"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_version(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json["version"] == "1.0.0"
    assert "environment" in response.json
