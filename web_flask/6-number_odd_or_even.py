#!/usr/bin/python3

"""Import flask"""
from flask import Flask, render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_template(n):
    return render_template("index.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    if n % 2 == 0:
        content = f"{n} is even"
    else:
        content = f"{n} is odd"
    return render_template("6-number_odd_or_even.html", content=content)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
