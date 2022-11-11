#!/usr/bin/python3
"""This module defines and runs a flask application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns 'Hello HBNB'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns 'C {text}'"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run()
