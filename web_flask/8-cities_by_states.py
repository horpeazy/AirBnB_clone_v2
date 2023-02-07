#!/usr/bin/python3
""" this module runs a sinple flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception=None):
    """ removes the datavase session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False,
           methods=['GET'])
def cities_by_states():
    """ renders all states and cities in the database"""
    query = storage.all(State)
    states = []
    for state in query.values():
        states.append(state)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
