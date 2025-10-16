from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_add():
    payload = {"a": 2, "b": 3}
    response = client.post("/add", json=payload)
    assert response.status_code == 200
    assert response.json()["sum"] == 5