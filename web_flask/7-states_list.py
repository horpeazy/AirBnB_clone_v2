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


@app.route('/states_list', strict_slashes=False,
           methods=['GET'])
def states_list():
    """ renders all states in the database"""
    query = storage.all(State)
    states = []
    for state in query.values():
        states.append(state)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
