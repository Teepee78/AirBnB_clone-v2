#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session():
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all('State')
    for state in states:
        print(state)
    return render_template('7-states_list.html')
