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

    assert data["message"] == "Task accepted for background execution"
    assert data["task_type"] == "api_health_check"


def test_run_task_with_unsupported_type():
    payload = {"task_type": "not_real"}

    response = client.post("/run-task", json=payload)
    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Task accepted for background execution"
    assert data["task_type"] == "not_real"


def test_tasks_endpoint_lists_multiple_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200

    data = response.json()
    task_types = [task["task_type"] for task in data["available_tasks"]]

    assert "api_health_check" in task_types
    assert "python_homepage_check" in task_types