#!/usr/bin/python3

"""Import flask"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Starts a flask web application"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def display_c(text):
    route_text = escape(text).replace("_", " ")
    return f"C {route_text}"


@app.route("/python/",
           defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route("/python/<string:text>",
           strict_slashes=False)
def python_route(text):
    route_variable = escape(text).replace("_", " ")
    return f"Python {route_variable}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
