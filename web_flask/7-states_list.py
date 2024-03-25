#!/usr/bin/python3
"""import modules to handle wsgi"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_cities():
    """render html page that lists out states"""
    states = storage.all("State")
    sorted_states = sorted(list(states.values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
