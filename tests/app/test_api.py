from fastapi.testclient import TestClient
import pytest

from src.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "App is up and running"}
