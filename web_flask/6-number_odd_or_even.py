#!/usr/bin/python3
"""imports for working with flask web framework"""

from flask import Flask, render_template
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
    return f"python {escape(new_txt)}"


@app.route('/number/<int:n>')
def display_number(n):
    """/number/<n>: display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        number = n
        return f"{number} is a number"


@app.route('/number_template/<int:n>')
def display_html(n):
    """/number/<n>: display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        number = n
        return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:n>')
def display_even_or_odd(n):
    """/number/<n>: display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        if n % 2 == 0:
            message = "is even"
            number = n
        if n % 2 != 0:
            number = n
            message = "is odd"
        return render_template(
            '6-number_odd_or_even.html',
            number=number, message=message
            )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
