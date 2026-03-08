from pydantic import BaseModel


class AutomationResult(BaseModel):
    task: str
    status: str