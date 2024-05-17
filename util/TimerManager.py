from util.timer_tm import Timer

class TimerManager:
    def __init__(self):
        self.timer_list = []

    def add_timer(self, name, due_time):
        self.timer_list.append(Timer(name, due_time))
