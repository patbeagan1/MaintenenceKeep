import time
import datetime

import timeago


class Task:
    def __init__(self, name: str, time_between_duedates: int, time_last_completed: int = 0):
        self.name = name
        self.time_between_duedates = time_between_duedates
        self.time_last_completed = time_last_completed

    def time_til_due(self):
        return self.time_last_completed + self.time_between_duedates - time.time()

    def time_til_due_percent(self):
        return self.time_til_due() / self.time_between_duedates

    def is_far_from_due(self):
        return self.time_til_due_percent() >= 0.5

    def is_close_to_due(self):
        percent = self.time_til_due_percent()
        return percent > 0.2 and percent <= 0.5

    def is_imminently_due(self):
        percent = self.time_til_due_percent()
        return percent > 0 and percent <= 0.2

    def is_overdue(self):
        return self.time_til_due_percent() < 0

    def formatted_task_time_left(self):
        seconds_remaining = self.time_til_due().__floor__()
        now = datetime.datetime.now()
        due = datetime.datetime.now() + datetime.timedelta(seconds=seconds_remaining)
        return timeago.format(due, now)

    @classmethod
    def from_filestring(filestring: str):
        attr = filestring.split(",")
        return Task(attr[0], int(attr[1]), int(attr[2]))

    def to_filestring(self):
        return f"{self.name},{self.time_between_duedates},{self.time_last_completed}"

    @classmethod
    def from_pandas_row(cls, x):
        return Task(x[0], x[1], x[2])
