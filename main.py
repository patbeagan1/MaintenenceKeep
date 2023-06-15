import argparse
import os

from flask import Flask, request

from routes.route_add_new_task import add_new_task
from routes.route_add_with_name import add_with_name
from routes.route_hello_world import hello_world
from routes.route_update_with_name import update_with_name
from routes.route_view_status import view_status
from routes.route_view_status_raw import view_status_raw
from routes.route_view_updates import view_updates
from util.datamanager import get_data_filename, set_data_filename

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


@app.route('/add_new_task')
def route_add_new_task(): return add_new_task()


@app.route('/add')
def route_add_with_name():
    name = request.args.get('name', '')
    duration = request.args.get('seconds', '')
    return add_with_name(name, duration)


@app.route('/help')
def route_help(): return help()


def check_file_empty(path_of_file):
    return os.path.exists(path_of_file) and os.stat(path_of_file).st_size == 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename',
        type=str,
        help='The name of the backing csv file')
    args = parser.parse_args()
    set_data_filename(args.filename)

    if check_file_empty(get_data_filename()):
        with open(get_data_filename(), "a") as f:
            f.write("task, recurrence, last_completed")

    app.run(host='0.0.0.0', debug=True)
