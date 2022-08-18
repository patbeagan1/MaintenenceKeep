import time

from style import style
from task_manager import TaskManager


def view_updates(name):
    _task_manager = TaskManager()
    matches = [time.gmtime(x.time_last_completed)
               for x in _task_manager.task_list_all
               if x.name == name]
    matches = [f"""<div class="taskrow">{time.strftime("%H:%M:%S %b %d, %Y (GMT %z)", x)}</div>"""
               for x in matches]
    items = "\n".join(matches)
    return f"""
    <html><style>{style()}</style><body>
    <div class="tasklist">
    <button onClick="location.href='/update/{name}'"/>
    <p>Update</p>
    </button>
    <h1>{name}</h1>
    {items}
    </div><body><html>  
    """
