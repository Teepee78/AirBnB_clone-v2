#!/usr/bin/python3
"""This module defines and runs a flask application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception):
    """
    Removes SQLAlchemy session
    """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<string:id>', strict_slashes=False)
def states(id=None):
    """Renders states list"""
    states = storage.all('State')
    if id is None:
        return render_template('7-states_list.html', states=states)
    else:
        state_key = "State.{}".format(id)
        if id in states:
            state = states[state_key]
            return render_template('9-states.html', states=[state, ])
        return render_template('9-states.html', states=None)


if __name__ == '__main__':
    app.run()
