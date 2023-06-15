import time

from routes.view_success import success, failure
from task.task_manager import TaskManager
from util.datamanager import get_data_filename


def update_with_name(name) -> str:
    task_manager = TaskManager()
    first = None
    for x in task_manager.task_list:
        if x.name == name:
            first = x
            break

    if not first:
        return failure(FileNotFoundError())

    with open(get_data_filename(), "a") as f:
        first.time_last_completed = time.time().__floor__()
        f.write("\n" + first.to_filestring())

    return success()
