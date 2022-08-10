import time

from system_status import generate_page
from task import Task
from task_manager import TaskManager


class Router:
    def hello_world(self):
        return 'Hello World!'

    def view_status(self):
        _task_manager = TaskManager()
        _task_manager.read_from_file()
        generate_page(_task_manager)
        _task_manager.write_to_file()
        with open("build/index.html", "r") as f:
            return f.read()

    def update_with_name(self, name) -> str:
        try:
            with open("build/data.txt", "r") as f:
                updated_lines = [
                    Task.from_filestring(line)
                    for line in f.readlines()
                ]

                matched_at_least_once = False
                for each in updated_lines:
                    if each.name == name:
                        matched_at_least_once = True
                        each.time_last_completed = time.time().__floor__()

                if not matched_at_least_once:
                    return "No matches"

                updated_lines = [
                    it.to_filestring()
                    for it in updated_lines
                ]

            with open("build/data.txt", "a") as f:
                f.write("\n".join(updated_lines))
            return "Success"
        except:
            return "Failure"

    def view_status_raw(self):
        with open("build/data.txt", "r") as f:
            return f.read()

    def add_with_name(self, name, duration):
        try:
            with open("build/data.txt", "a") as f:
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
