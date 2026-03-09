from pydantic import BaseModel


class AutomationTaskRequest(BaseModel):
    task_type: str


class AutomationResult(BaseModel):
    task: str
    status: str
    checked_url: str