import os

from flask import Flask

from usecase.add_with_name import add_with_name
from usecase.hello_world import hello_world
from usecase.help import help
from usecase.update_with_name import update_with_name
from usecase.view_status import view_status
from usecase.view_status_raw import view_status_raw
from usecase.view_updates import view_updates

app = Flask(__name__)


@app.route('/hello')
def route_hello_world(): return hello_world()


@app.route('/status/raw')
def route_view_status_raw(): return view_status_raw()


@app.route('/status')
@app.route('/')
def route_view_status(): return view_status()


@app.route('/update/<name>')
def route_update_with_name(name: str): return update_with_name(name)


@app.route('/view_updates/<name>')
def route_view_updates(name: str): return view_updates(name)


@app.route('/add/<name>/<duration>')
def route_add_with_name(name: str, duration: int): return add_with_name(name, duration)


@app.route('/help')
def route_help(): return help()


def check_file_empty(path_of_file):
    return os.path.exists(path_of_file) and os.stat(path_of_file).st_size == 0


if __name__ == '__main__':
    csv = "build/data.csv"
    if check_file_empty(csv):
        with open(csv, "a") as f:
            f.write("task, recurrence, last_completed")

    app.run()
