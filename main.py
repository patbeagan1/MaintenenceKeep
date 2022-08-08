import time

from task import Task
from task_manager import TaskManager
from times import second


def generate_page():
    with open("assets/style.css", "r") as f:
        style = f.read()
    with open("build/index.html", "w") as f:
        f.write(f"<html><style>{style}</style><body>")
        for task in _task_manager.task_list:
            if task.is_far_from_due(): due_time_indicator = "far_from_due"
            if task.is_close_to_due(): due_time_indicator = "close_to_due"
            if task.is_imminently_due(): due_time_indicator = "imminently_due"
            if task.is_overdue(): due_time_indicator = "overdue"
            f.write(f"""
<div class="taskrow">
  <div class="task-indicator {due_time_indicator}"></div>
  <div class="task">{task.name}</div>
  <div class="task" style="float: right">{time.localtime(task.time_til_due())}</div>
</div>""")
        f.write("</body></html>")


if __name__ == '__main__':
    _task_manager = TaskManager()
    _task_manager.read_from_file()
    _task_manager.task_list.append(Task("testing", 10 * second, time.time().__floor__()))
    generate_page()
    _task_manager.write_to_file()
