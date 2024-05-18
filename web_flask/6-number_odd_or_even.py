#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on localhost, port 5000.
"""
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def default():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_path(text):
    """C path"""
    modified_text = text.replace('_', ' ')
    return f'C {modified_text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_path(text="is cool"):
    """python path'"""
    modified_text = text.replace('_', ' ')
    return f'Python {modified_text}'


@app.route('/number/<int:n>')
def number_path_int(n):
    return f"{n} is a number"


@app.route('/number/<string:n>')
def number_path_not_int(n):
    abort(404)


@app.route('/number_template/<int:n>')
def number_template_int(n):
    return render_template("5-number.html", n=n)


@app.route('/number_template/<string:n>')
def number_template_not_int(n):
    abort(404)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even_int(n):
    return render_template("6-number_odd_or_even.html", num=n)


@app.route('/number_odd_or_even/<string:n>')
def number_odd_or_even_not_int(n):
    abort(404)


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
