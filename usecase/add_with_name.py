import time

from datamanager import DataManager
from task import Task
from task_manager import TaskManager


def add_with_name(name, duration, task_manager: TaskManager):
    try:
        task_manager.submit(Task(name, duration, time.time().__floor__()))
        return "Success"
    except Exception as e:
        return f"Failure {e}"
