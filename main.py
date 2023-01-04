from flask import Flask

from datamanager import DataManager
from task_manager import TaskManager
from usecase.add_with_name import add_with_name
from usecase.hello_world import hello_world
from usecase.help import help
from usecase.update_with_name import update_with_name
from usecase.view_status import view_status
from usecase.view_status_raw import view_status_raw
from usecase.view_updates import view_updates

app = Flask(__name__)
tm = TaskManager()


@app.route('/hello')
def route_hello_world(): return hello_world()


@app.route('/status/raw.csv')
def route_view_status_raw(): return view_status_raw(tm)


@app.route('/status')
@app.route('/')
def route_view_status(): return view_status(tm)


@app.route('/update/<name>')
def route_update_with_name(name: str): return update_with_name(name, tm)


@app.route('/view_updates/<name>')
def route_view_updates(name: str): return view_updates(name, tm)


@app.route('/add/<name>/<duration>')
def route_add_with_name(name: str, duration: int): return add_with_name(name, duration, tm)


@app.route('/help')
def route_help(): return help()


if __name__ == '__main__':
    dm = DataManager()
    dm.check_sqlite()
    # app.run(host='0.0.0.0', debug=True)
    app.run()
