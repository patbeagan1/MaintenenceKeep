from task_manager import TaskManager


def generate_page(task_manager: TaskManager):
    with open("assets/style.css", "r") as f:
        style = f.read()
    with open("build/index.html", "w") as f:
        f.write(f"<html><style>{style}</style><body><div class=\"tasklist\">")
        for task in task_manager.task_list:
            if task.is_far_from_due(): due_time_indicator = "far_from_due"
            if task.is_close_to_due(): due_time_indicator = "close_to_due"
            if task.is_imminently_due(): due_time_indicator = "imminently_due"
            if task.is_overdue(): due_time_indicator = "overdue"

            f.write(f"""
<div class="taskrow">
  <div class="task-indicator {due_time_indicator}"></div>
  <div class="task">{task.name}</div>
  <div class="task-timer">{task.formatted_task_time_left()}</div>
</div>""")
        f.write("</div></body></html>")


