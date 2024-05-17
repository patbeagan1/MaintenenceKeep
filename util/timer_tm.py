# Add necessary methods to manage timers


import time


class Timer:
    def __init__(self, name, due_time):
        self.name = name
        self.due_time = due_time  # due_time should be a timestamp

    def time_left(self):
        return self.due_time - time.time()

    def formatted_timer_time_left(self):
        time_left = max(0, self.time_left())
        minutes, seconds = divmod(int(time_left), 60)
        return f"{minutes:02}:{seconds:02}"
