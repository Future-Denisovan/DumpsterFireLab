import pytest
from app.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_roll_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_roll_contains_dice_result(client):
    response = client.get("/")
    html = response.data.decode()
    assert "You rolled a" in html

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
