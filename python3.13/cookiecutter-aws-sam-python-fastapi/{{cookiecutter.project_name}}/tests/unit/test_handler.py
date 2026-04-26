from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World", "Framework": "FastAPI on Python 3.13"}


def test_read_item():
    response = client.get("/items/42", params={"q": "sam"})

    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "sam"}
