import time

from routes.view_success import success, failure
from task.task import Task
from util.datamanager import get_data_filename


def add_with_name(name, duration):
    try:
        int(duration)
        with open(get_data_filename(), "a") as f:
            f.write("\n" + Task(name, duration, time.time().__floor__()).to_filestring())
        return success()
    except Exception as e:
        return failure(e)
