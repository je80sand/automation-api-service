import time


def run_sample_automation():
    """
    Example automation task.
    This simulates a job like scraping, monitoring, or testing.
    """

    print("Starting automation task...")

    time.sleep(2)

    result = {
        "task": "sample_automation",
        "status": "completed"
    }

    print("Automation finished.")

    return result