import logging
import requests

logger = logging.getLogger(__name__)


def run_api_health_check():
    logger.info("Starting automation task: api_health_check")

    url = "https://api.github.com"
    response = requests.get(url)

    status = "healthy" if response.status_code == 200 else "unhealthy"

    result = {
        "task": "api_health_check",
        "checked_url": url,
        "status": status
    }

    logger.info("Automation task completed: api_health_check")
    return result


TASK_REGISTRY = {
    "api_health_check": run_api_health_check,
}


def run_task_by_type(task_type: str):
    logger.info("Received task request: %s", task_type)

    task_function = TASK_REGISTRY.get(task_type)

    if task_function is None:
        logger.error("Unsupported task type: %s", task_type)
        return {
            "task": task_type,
            "checked_url": "",
            "status": "unsupported"
        }

    return task_function()