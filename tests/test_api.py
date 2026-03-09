from unittest.mock import patch, Mock

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


@patch("app.automation_tasks.requests.get")
def test_run_task_endpoint(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    payload = {"task_type": "api_health_check"}

    response = client.post("/run-task", json=payload)
    assert response.status_code == 200

    data = response.json()

    assert "result" in data
    assert data["result"]["task"] == "api_health_check"
    assert data["result"]["status"] == "healthy"
    assert data["result"]["checked_url"] == "https://api.github.com"


def test_run_task_with_unsupported_type():
    payload = {"task_type": "not_real"}

    response = client.post("/run-task", json=payload)
    assert response.status_code == 200

    data = response.json()

    assert data["result"]["task"] == "not_real"
    assert data["result"]["status"] == "unsupported"
    assert data["result"]["checked_url"] == ""