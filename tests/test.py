from src.main import app
from fastapi.testclient import TestClient


def test_health():
    client = TestClient(app)
    response = client.get("/health")
    result = {"status": "ok"}
    assert response.status_code == 200
    assert response.json() == result
