from util.TimerManager import TimerManager
from task.task_manager import TaskManager
from util.style import style


def view_timers(_timer_manager):
    output = []
    output.append(f'<html><style>{style()}</style><body><div class="timerlist">')
    for timer in _timer_manager.timer_list:
        print(timer)
        time_left = timer.time_left()
        if time_left > 3600:
            due_time_indicator = "far_from_due"
        elif 600 < time_left <= 3600:
            due_time_indicator = "close_to_due"
        elif 0 < time_left <= 600:
            due_time_indicator = "imminently_due"
        else:
            due_time_indicator = "overdue"

        output.append(
            f"""
            <div class="timerrow">
              <div class="timer-indicator {due_time_indicator}"></div>
              <a href="/view_updates/{timer.name}"><div class="timer">{timer.name}</div></a>
              <div class="timer-countdown" id="countdown_{timer.name}">due {timer.formatted_timer_time_left()}</div>
           
            </div>"""
        )
    output.append(
        """
        <br>
        <a href="/add_new_timer">Add a new timer</a>
        """
    )
    output.append("</div>")
    output.append("</body></html>")
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
    """
