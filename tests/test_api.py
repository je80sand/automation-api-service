from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Automation API Service is running"}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_run_task_endpoint():
    response = client.post("/run-task")
    assert response.status_code == 200

    data = response.json()

    assert "result" in data
    assert data["result"]["task"] == "api_health_check"
    assert data["result"]["status"] == "healthy"
    assert data["result"]["checked_url"] == "https://api.github.com"