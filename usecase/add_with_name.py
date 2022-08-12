import time

from task import Task


def add_with_name(name, duration):
    try:
        with open("build/data.csv", "a") as f:
            f.write("\n" + Task(name, duration, time.time().__floor__()).to_filestring())
        return "Success"
    except Exception as e:
        return f"Failure {e}"
