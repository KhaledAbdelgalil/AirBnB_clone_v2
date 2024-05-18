#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on localhost, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'.
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

if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
