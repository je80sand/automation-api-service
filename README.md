# Automation API Service

A Python-based REST API built with FastAPI for running automation tasks, tracking execution history, and exposing operational metrics.

This project simulates a lightweight internal automation platform: clients can discover available tasks, trigger checks in the background, review run history, and inspect simple service metrics.

---

## Features

- FastAPI backend service
- Modular project structure
- Background automation task execution
- Task registry with metadata
- Task discovery endpoint
- Run history tracking
- Metrics endpoint
- Health endpoint
- Input validation with Pydantic
- Logging for automation task execution
- Pytest automated test suite
- Mocked external API calls in tests
- GitHub Actions CI pipeline

---

## Current Automation Tasks

**api_health_check**

Checks the health of the GitHub API.

**python_homepage_check**

Checks the availability of python.org.

---

## API Endpoints

### GET /

Returns the root service message.

### GET /health

Returns service health status.

### GET /tasks

Lists available automation tasks and descriptions.

### POST /run-task

Accepts an automation task request and schedules it for background execution.

### GET /runs

Returns automation task run history.

### GET /metrics

Returns task execution metrics such as total runs and success rate.

---

## Example Request

```json
{
  "task_type": "api_health_check"
}
```

---

## Example Response

```json
{
  "message": "Task accepted for background execution",
  "task_type": "api_health_check"
}
```

---

## Example Run History

```json
{
  "runs": [
    {
      "task": "api_health_check",
      "status": "healthy",
      "timestamp": "2026-03-09T16:27:17.549017+00:00"
    }
  ]
}
```

---

## Example Metrics Response

```json
{
  "total_runs": 4,
  "successful_runs": 4,
  "failed_runs": 0,
  "success_rate": "100%"
}
```

---

## Architecture

```
Client / Swagger UI / API Consumer
                │
                ▼
        FastAPI Application
                │
     ┌──────────┼──────────┐
     ▼ ▼ ▼
  /tasks /run-task /metrics
                │
                ▼
        Task Registry Engine
                │
     ┌──────────┴──────────┐
     ▼ ▼
api_health_check python_homepage_check
     │ │
     ▼ ▼
 GitHub API python.org
                │
                ▼
          Run History Store
```

---

## Project Structure

```
automation-api-service
│
├── .github
│ └── workflows
│ └── ci.yml
│
├── app
│ ├── __init__.py
│ ├── automation_tasks.py
│ ├── main.py
│ ├── models.py
│ └── routes.py
│
├── tests
│ └── test_api.py
│
├── Dockerfile
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Running Locally

Install dependencies

```
pip install -r requirements.txt
```

Start the API

```
uvicorn app.main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Running Tests

```
pytest
```

---

## Real API Usage

Run GitHub API health check

```
curl -X POST http://127.0.0.1:8000/run-task \
-H "Content-Type: application/json" \
-d '{"task_type":"api_health_check"}'
```

View run history

```
curl http://127.0.0.1:8000/runs
```

View metrics

```
curl http://127.0.0.1:8000/metrics
```

---

## CI

This repository includes a GitHub Actions workflow that automatically runs tests when code is pushed.

---

## Author

Jose Sandoval  
GitHub: https://github.com/je80sand