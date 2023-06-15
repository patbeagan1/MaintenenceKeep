from task.task_manager import TaskManager
from util.style import style


def view_status():
    _task_manager = TaskManager()
    output = []
    output.append(f"<html><style>{style()}</style><body><div class=\"tasklist\">")
    for task in _task_manager.task_list:
        due_time_indicator = "Unknown"
        if task.is_far_from_due(): due_time_indicator = "far_from_due"
        if task.is_close_to_due(): due_time_indicator = "close_to_due"
        if task.is_imminently_due(): due_time_indicator = "imminently_due"
        if task.is_overdue(): due_time_indicator = "overdue"

        output.append(f"""
            <div class="taskrow">
              <div class="task-indicator {due_time_indicator}"></div>
              <a href="/view_updates/{task.name}"><div class="task">{task.name}</div></a>
              <div class="task-timer">due {task.formatted_task_time_left()}</div>
            </div>""")
    output.append("""
        <br>
        <a href="/add_new_task">Add a new task</a>
        """)
    output.append("</div>")
    output.append("</body></html>")
    return "".join(output)
