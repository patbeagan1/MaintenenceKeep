import pandas
from pandas import DataFrame

from datamanager import DataManager
from task import Task


class TaskManager:
    def __init__(self):
        self.data_manager = DataManager()

    def dataframe(self):
        return self.data_manager.get_dataframe()

    def task_list_all(self):
        return [
            Task.from_pandas_row(x)
            for x in self.dataframe().itertuples(index=False)
        ]

    def task_list(self):
        task_list = [
            Task.from_pandas_row(x)
            for x in self.dataframe().groupby("task").max().itertuples()
        ]
        task_list.sort(key=lambda x: x.time_til_due_percent())
        return task_list

    def read_all(self):
        return self.data_manager.read_all()

    def submit(self, task: Task):
        self.data_manager.submit_to_file(task)
