from fastapi import APIRouter
from app.automation_tasks import run_sample_automation

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/run-task")
def run_task():
    result = run_sample_automation()
    return {"result": result}