from datamanager import DataManager
from task_manager import TaskManager


def view_status_raw(task_manager: TaskManager):
    return task_manager.read_all()