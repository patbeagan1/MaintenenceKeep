from routes.route_view_status import view_status
from util.TimerManager import TimerManager
from task.task_manager import TaskManager
from util.style import style


import time
def add_new_timer():
    output = []
    output.append(f"<html><style>{style()}</style><body><div class=\"add-timer\">")
    output.append("""
        <h2>Add a New Timer</h2>
        <form action="/save_new_timer" method="post">
            <label for="name">Timer Name:</label><br>
            <input type="text" id="name" name="name"><br><br>
            <label for="duration">Duration (seconds):</label><br>
            <input type="number" id="duration" name="duration"><br><br>
            <input type="submit" value="Add Timer">
        </form>
        <br>
        <a href="/">Back to Timer List</a>
        """)
    output.append("</div></body></html>")
    return "".join(output)

def style():
    return """
    .timerlist { font-family: Arial, sans-serif; }
    .timerrow { margin: 10px; padding: 10px; border: 1px solid #ccc; }
    .timer-indicator.far_from_due { background-color: green; }
    .timer-indicator.close_to_due { background-color: yellow; }
    .timer-indicator.imminently_due { background-color: orange; }
    .timer-indicator.overdue { background-color: red; }
    .timer { display: inline-block; width: 200px; }
    .timer-countdown { display: inline-block; width: 100px; }
    .add-timer { font-family: Arial, sans-serif; margin: 20px; padding: 20px; border: 1px solid #ccc; }
    """


def save_new_timer(request, _timer_manager):
    name = request.form['name']
    duration = int(request.form['duration'])
    due_time = time.time() + duration
    _timer_manager.add_timer(name, due_time)

    return view_status()
