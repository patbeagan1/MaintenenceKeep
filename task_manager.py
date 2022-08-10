import typing

from pandas import DataFrame

from task import Task
import pandas as pd


class TaskManager:
    def __init__(self):
        self.task_list = []
        self.filename = "build/data.csv"

        d = pd.read_csv(self.filename)
        d = typing.cast(DataFrame, d)
        self.dataframe = d

        d = d.groupby("task").max()
        for x in d.itertuples():
            self.task_list.append(Task.from_pandas_row(x))
