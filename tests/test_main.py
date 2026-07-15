"""Unit tests for the FastAPI service."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert "version" in body


def test_greet_ok():
    resp = client.get("/greet/Ada")
    assert resp.status_code == 200
    assert resp.json() == {"greeting": "Hello, Ada!"}


def test_greet_blank_name():
    resp = client.get("/greet/%20")
    assert resp.status_code == 400


def test_sum_ok():
    resp = client.post("/sum", json={"numbers": [1, 2, 3.5]})
    assert resp.status_code == 200
    assert resp.json() == {"total": 6.5}


def test_sum_empty():
    resp = client.post("/sum", json={"numbers": []})
    assert resp.status_code == 400


def test_echo():
    resp = client.post("/echo", json={"message": "ping"})
    assert resp.status_code == 200
    assert resp.json() == {"echo": "ping"}
