import pytest
from src.main import app
from src.models import Resistar_data
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def sample_data():
    data1 = Resistar_data(title="sampleTitle1", done=False)
    data2 = Resistar_data(title="sampleTitle2", done=True)
    return [data1, data2]


def test_health():
    client = TestClient(app)
    response = client.get("/health")
    result = {"status": "ok"}
    assert response.status_code == 200
    assert response.json() == result


def test_post_autofill(sample_data):
    client = TestClient(app)
    response = client.post("/todos/", json=sample_data[0].dict())
    assert response.status_code == 200
    assert response.json()["title"] == "sampleTitle1"
