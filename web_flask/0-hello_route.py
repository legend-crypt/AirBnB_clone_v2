#!/usr/bin/python3

"""Import flask"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Starts a flask web application"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
