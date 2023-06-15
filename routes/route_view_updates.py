import time

from task.task_manager import TaskManager
from util.style import style


def view_updates(name):
    _task_manager = TaskManager()
    matches = [time.localtime(x.time_last_completed)
               for x in _task_manager.task_list_all
               if x.name == name]
    time_string = "%c"
    matches = [f"""<div class="taskrow">{time.strftime(time_string, x)}</div>"""
               for x in matches]
    items = "\n".join(matches)
    return f"""
    <html><style>{style()}</style><body><div class="tasklist">
        <button onClick="location.href='/update/{name}'"/>
        <p>Update</p>
        </button>
        <h1>{name}</h1>
        {items}
    </div><body><html>  
    """
