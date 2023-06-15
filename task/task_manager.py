import typing

from pandas import DataFrame

import pandas as pd

from task.task import Task
from util.datamanager import get_data_filename


class TaskManager:
    def __init__(self):
        self.filename = get_data_filename()
        self.setup_dataframe()
        self.task_list = [
            Task.from_pandas_row(x)
            for x in self.dataframe.groupby("task").max().itertuples()
        ]
        self.task_list.sort(key=lambda x: x.time_til_due_percent())
        self.task_list_all = [
            Task.from_pandas_row(x)
            for x in self.dataframe.itertuples(index=False)
        ]

    def setup_dataframe(self):
        d = pd.read_csv(self.filename)
        d = typing.cast(DataFrame, d)
        self.dataframe = d
