#!/usr/bin/python3
"""imports for working with flask web framework"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def run_web():
    """runs a flask server on port 0.0.0.0:5000"""
    return "Hello HBNB"

@app.route('/hbnb')
def display_hbnb():
    """
    display a a text when a user navigate to the hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)