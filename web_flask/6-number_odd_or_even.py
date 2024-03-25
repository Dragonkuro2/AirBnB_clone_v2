#!/usr/bin/python3
""" script that listen on IP 0.0.0.0 and port 5000
    using flask, and it'll display something on required page
    depands on the URL, """

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    """ Function that returns 'n is a number' only if the path has a number """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_tmp(n):
    """ Function that returns a jinja template. """
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ Function that returns if the number is odd or even. """
    if n % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    return render_template('6-number_odd_or_even.html', number=n,
                           even_odd=even_odd)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
