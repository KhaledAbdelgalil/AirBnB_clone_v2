#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on localhost, port 5000.
"""
from flask import Flask

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


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
