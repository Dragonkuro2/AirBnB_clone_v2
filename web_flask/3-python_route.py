#!/usr/bin/python3
""" script that listen on IP 0.0.0.0 and port 5000
    using flask, and it'll display something on required page
    depands on the URL, """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Simple function that returns 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ Function that returns 'HBNB'. """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_route(text):
    """ Function that returns 'C' + the rest of the link """
    return "C %s" % text.replace("_", " ")

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_is_cool(text='is cool'):
    """ Function that resturs 'python' + the rest of the link
        or 'is cool' by default """
    return "Python %s" % text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
