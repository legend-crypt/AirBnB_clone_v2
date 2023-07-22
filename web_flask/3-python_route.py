#!/usr/bin/python3
"""imports for working with flask web framework"""

from flask import Flask
from markupsafe import escape


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


@app.route('/c/<text>')
def display_C_text(text):
    """
    display a a text when a user navigate to hbnb page
    """
    new_txt = text.replace('_', ' ')
    return f"C {escape(new_txt)}"


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def display_python_text(text):
    """
    display a a text when a user navigate to hbnb page
    """
    new_txt = text.replace('_', ' ')
    return f"Python {escape(new_txt)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
