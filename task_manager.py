import typing

from pandas import DataFrame

from task import Task
import pandas as pd


class TaskManager:
    def __init__(self):
        self.filename = "build/data.csv"
        self.setup_dataframe()
        self.task_list = [
            Task.from_pandas_row(x)
            for x in self.dataframe.groupby("task").max().itertuples()
        ]
        self.task_list_all = [
            Task.from_pandas_row(x)
            for x in self.dataframe.itertuples(index=False)
        ]


    def setup_dataframe(self):
        d = pd.read_csv(self.filename)
        d = typing.cast(DataFrame, d)
        self.dataframe = d
