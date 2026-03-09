from fastapi import APIRouter
from app.automation_tasks import run_task_by_type, get_available_tasks
from app.models import AutomationTaskRequest

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/tasks")
def list_tasks():
    return {"available_tasks": get_available_tasks()}


@router.post("/run-task")
def run_task(task_request: AutomationTaskRequest):
    result = run_task_by_type(task_request.task_type)
    return {"result": result}