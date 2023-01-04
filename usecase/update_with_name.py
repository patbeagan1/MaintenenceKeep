import time

from datamanager import DataManager
from task_manager import TaskManager


def update_with_name(name: str, task_manager: TaskManager) -> str:
    first = None
    for x in (task_manager.task_list()):
        if x.name == name:
            first = x
            break

    if not first:
        return "Failure, not found"

    first.time_last_completed = time.time().__floor__()
    task_manager.submit(first)

    return "Success"
