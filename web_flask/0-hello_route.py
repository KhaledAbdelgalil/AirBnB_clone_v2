#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on localhost, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def default():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="localhost")
