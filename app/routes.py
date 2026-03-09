from fastapi import APIRouter, BackgroundTasks

from app.automation_tasks import (
    get_available_tasks,
    get_run_history,
    run_task_by_type,
)
from app.models import AutomationTaskRequest

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "automation-api-service"
    }


@router.get("/tasks")
def list_tasks():
    return {"available_tasks": get_available_tasks()}


@router.get("/runs")
def list_runs():
    return {"runs": get_run_history()}


@router.post("/run-task")
async def run_task(task_request: AutomationTaskRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(run_task_by_type, task_request.task_type)
    return {
        "message": "Task accepted for background execution",
        "task_type": task_request.task_type
    }

@router.get("/metrics")
def metrics():
    runs = get_run_history()

    total_runs = len(runs)
    successful_runs = len([r for r in runs if r["status"] == "healthy"])
    failed_runs = total_runs - successful_runs

    success_rate = "0%"

    if total_runs > 0:
        success_rate = f"{round((successful_runs / total_runs) * 100)}%"

    return {
        "total_runs": total_runs,
        "successful_runs": successful_runs,
        "failed_runs": failed_runs,
        "success_rate": success_rate
    }