import logging
import requests

logger = logging.getLogger(__name__)

def run_sample_automation():
    logger.info("Starting API health check automation")

    url = "https://api.github.com"

    response = requests.get(url)

    status = "healthy" if response.status_code == 200 else "unhealthy"

    result = {
        "task": "api_health_check",
        "checked_url": url,
        "status": status
    }

    logger.info("Automation task completed")

    return result