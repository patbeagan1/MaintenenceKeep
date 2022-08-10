import time

from system_status import generate_page
from task import Task
from task_manager import TaskManager


class Router:
    def hello_world(self):
        return 'Hello World!'

    def view_status(self):
        _task_manager = TaskManager()
        generate_page(_task_manager)
        with open("build/index.html", "r") as f:
            return f.read()

    def update_with_name(self, name) -> str:
        task_manager = TaskManager()
        already_exists = any(x.name == name for x in (task_manager.task_list))

        if not already_exists:
            return "Failure, not found"

        with open("build/data.csv", "a") as f:
            f.write("")

        return "Success"

    def view_status_raw(self):
        with open("build/data.csv", "r") as f:
            return f.read()

    def add_with_name(self, name, duration):
        try:
            with open("build/data.csv", "a") as f:
                f.write(Task(name, duration, time.time().__floor__()).to_filestring())
            return "Success"
        except Exception as e:
            return f"Failure {e}"

    def help(self):
        return """
            <html>
            <body>
            <a href="http://localhost:5000/add/testing/120"><p>Add task</p></a>
            <a href="http://localhost:5000/update/testing"><p>Update task</p></a>
            <a href="http://localhost:5000/"><p>Check Status</p></a>
            </body>
            </html>
            """
