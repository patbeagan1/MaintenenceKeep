import time

from task_manager import TaskManager


def update_with_name(name) -> str:
    task_manager = TaskManager()
    first = None
    for x in (task_manager.task_list):
        if x.name == name:
            first = x
            break

    if not first:
        return "Failure, not found"

    with open("build/data.csv", "a") as f:
        first.time_last_completed = time.time().__floor__()
        f.write("\n" + first.to_filestring())

    return "Success"