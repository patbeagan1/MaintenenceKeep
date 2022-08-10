from router import Router

from flask import Flask

app = Flask(__name__)
router = Router()


@app.route('/hello')
def hello_world(): return router.hello_world()


@app.route('/status/raw')
def view_status_raw(): return router.view_status_raw()


@app.route('/status')
@app.route('/')
def view_status(): return router.view_status()


@app.route('/update/<name>')
def update_with_name(name: str): return router.update_with_name(name)


@app.route('/add/<name>/<duration>')
def add_with_name(name: str, duration: int): return router.add_with_name(name, duration)


@app.route('/help')
def help(): return router.help()


if __name__ == '__main__':
    app.run()
