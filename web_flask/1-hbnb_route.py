#!/usr/bin/python3
""" Script that listen on IP 0.0.0.0 and port 5000
    using flask framwork and display some output depending on the path."""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Simple function that returns 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ Simple function that returns 'HBNB' """
    return "HBNB"


if __name__ == "__main__":
    app.run()
