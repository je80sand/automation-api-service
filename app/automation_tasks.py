import logging
from datetime import datetime, UTC
import requests

logger = logging.getLogger(__name__)

RUN_HISTORY = []


def record_run(task_name: str, status: str):
    RUN_HISTORY.append(
        {
            "task": task_name,
            "status": status,
            "timestamp": datetime.now(UTC).isoformat()
        }
    )


async def run_api_health_check():
    logger.info("Starting automation task: api_health_check")

    url = "https://api.github.com"
    response = requests.get(url)

    status = "healthy" if response.status_code == 200 else "unhealthy"

    result = {
        "task": "api_health_check",
        "checked_url": url,
        "status": status
    }

    record_run(result["task"], result["status"])

    logger.info("Automation task completed: api_health_check")
    return result


async def run_python_homepage_check():
    logger.info("Starting automation task: python_homepage_check")

    url = "https://www.python.org"
    response = requests.get(url)

    status = "healthy" if response.status_code == 200 else "unhealthy"

    result = {
        "task": "python_homepage_check",
        "checked_url": url,
        "status": status
    }

    record_run(result["task"], result["status"])

    logger.info("Automation task completed: python_homepage_check")
    return result


TASK_REGISTRY = {
    "api_health_check": {
        "handler": run_api_health_check,
        "description": "Checks the health of the GitHub API"
    },
    "python_homepage_check": {
        "handler": run_python_homepage_check,
        "description": "Checks the availability of python.org"
    }
}


def get_available_tasks():
    return [
        {
            "task_type": task_name,
            "description": task_data["description"]
        }
        for task_name, task_data in TASK_REGISTRY.items()
    ]


def get_run_history():
    return RUN_HISTORY


async def run_task_by_type(task_type: str):
    logger.info("Received task request: %s", task_type)

    task_data = TASK_REGISTRY.get(task_type)

    if task_data is None:
        logger.error("Unsupported task type: %s", task_type)
        unsupported_result = {
            "task": task_type,
            "checked_url": "",
            "status": "unsupported"
        }

        record_run(unsupported_result["task"], unsupported_result["status"])
        return unsupported_result

    task_function = task_data["handler"]
    return await task_function()