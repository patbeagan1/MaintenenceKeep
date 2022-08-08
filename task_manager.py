from task import Task


class TaskManager:
    def __init__(self):
        self.task_list = []
        self.filename = "build/data.txt"

    def read_from_file(self):
        with open(self.filename, "r") as f:
            for line in f.readlines():
                self.task_list.append(Task.from_filestring(line))

    def write_to_file(self):
        with open(self.filename, "w") as f:
            for task in self.task_list:
                f.write(task.to_filestring() + "\n")
