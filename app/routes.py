from fastapi import APIRouter
from app.automation_tasks import run_task_by_type, get_available_tasks, get_run_history
from app.models import AutomationTaskRequest

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/tasks")
def list_tasks():
    return {"available_tasks": get_available_tasks()}


@router.get("/runs")
def list_runs():
    return {"runs": get_run_history()}


@router.post("/run-task")
async def run_task(task_request: AutomationTaskRequest):
    result = await run_task_by_type(task_request.task_type)
    return {"result": result}