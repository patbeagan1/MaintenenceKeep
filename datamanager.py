import os
import typing

import pandas as pd
from pandas import DataFrame

from task import Task


class DataManager():
    def __init__(self):
        self.filename = "build/data.csv"

    def get_dataframe(self) -> DataFrame:
        d = pd.read_csv(self.filename)
        return typing.cast(DataFrame, d)

    def check_file_empty(self):
        return os.path.exists(self.filename) and os.stat(self.filename).st_size == 0

    def ensure_file(self):
        if self.check_file_empty(self.filename):
            with open(self.filename, "a") as f:
                f.write("task, recurrence, last_completed")

    def check_sqlite(self):
        import _sqlite3
        print(_sqlite3.SQLITE_OK)
        memory_db = ":memory:"
        disk_db = "/tmp/maintenence-db"
        db = _sqlite3.connect(disk_db)
        db.execute("create table HELLO (int)")
        db.execute("insert into HELLO values(345)")
        db.commit()
        a = db.execute("select * from HELLO").fetchall()
        print(a)

    def create_table(self):
        pass

    def read_all(self):
        with open("build/data.csv", "r") as f:
            return f.read()

    def submit_to_file(self, task: Task):
        with open("build/data.csv", "a") as f:
            f.write("\n" + task.to_filestring())
