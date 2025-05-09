import pytest
from src.main import app, todos
from src.models import TodoItem
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def sample_data():
    data1 = TodoItem(title="sampleTitle1", done=False)
    data2 = TodoItem(title="sampleTitle2", done=True)
    return [data1, data2]


@pytest.fixture(autouse=True)
def reset_todos():
    todos.clear()


def set_sampledata(item):
    client = TestClient(app)
    for index, data in enumerate(item):
        response = client.post("/todos/", json=data.model_dump())
        assert response.status_code == 200

    return client, response


def test_health():
    client = TestClient(app)
    response = client.get("/health")
    result = {"status": "ok"}
    assert response.status_code == 200
    assert response.json() == result


def test_post_title_and_done(sample_data):
    client = TestClient(app)
    response = client.post("/todos/", json=sample_data[0].model_dump())
    assert response.status_code == 200
    assert response.json()[0]["title"] == "sampleTitle1"
    assert response.json()[0]["done"] == False


def test_post_data_registory(sample_data):
    client, _ = set_sampledata(sample_data)
    get_response = client.get("/todos")
    assert get_response.status_code == 200

    result_list = get_response.json()
    for receive, sent in zip(result_list, sample_data):
        assert receive == sent.model_dump()


def test_post_data_delete_by_index(sample_data):
    client, _ = set_sampledata(sample_data)

    for i in range(len(sample_data)):
        res_before = client.get("/todos")
        assert res_before.status_code == 200
        current_list = res_before.json()
        assert len(current_list) == len(sample_data) - i

        delete_list = client.delete("/todos/by-index/0")
        assert delete_list.status_code == 200


def test_post_data_delete_by_id(sample_data):
    client, _ = set_sampledata(sample_data)

    for i in range(len(sample_data)):
        res_before = client.get("/todos")
        assert res_before.status_code == 200
        current_list = res_before.json()
        assert len(current_list) == len(sample_data) - i
        id = current_list[0]["id"]
        delete_list = client.delete("/todos/" + id)
        assert delete_list.status_code == 200


def test_update_data_by_index(sample_data):
    client, _ = set_sampledata(sample_data)
    for i in range(len(sample_data)):
        update_text = "updatetext" + str(i + 1)
        update_index = "/todos/by-index/" + str(i)
        update_sample_data = TodoItem(title=update_text, done=True)
        update_response = client.patch(
            update_index, json=update_sample_data.model_dump()
        )
        assert update_response.status_code == 200

        get_response = client.get("/todos")
        assert get_response.status_code == 200

        result_list = get_response.json()
        assert result_list[i]["title"] == update_text
        assert result_list[i]["done"] == True


def test_update_data_by_id(sample_data):
    client, _ = set_sampledata(sample_data)
    res_before = client.get("/todos")
    current_list = res_before.json()
    for i in range(len(sample_data)):
        update_text = "updatetext" + str(i + 1)
        id = current_list[i]["id"]
        update_sample_data = TodoItem(title=update_text, done=True)
        update_response = client.patch(
            "/todos/" + id, json=update_sample_data.model_dump()
        )
        assert update_response.status_code == 200

        get_response = client.get("/todos")
        assert get_response.status_code == 200

        result_list = get_response.json()
        assert result_list[i]["title"] == update_text
        assert result_list[i]["done"] == True
