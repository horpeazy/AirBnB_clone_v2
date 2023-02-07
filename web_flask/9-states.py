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


@app.route('/states/<id>', strict_slashes=False,
           methods=['GET'])
@app.route('/states', strict_slashes=False,
           methods=['GET'])
def states(id=None):
    """ renders all states in the database"""
    query = storage.all(State)
    states = []
    for state in query.values():
        states.append(state)
    if id:
        state_obj = None
        for state in states:
            if state.id == id:
                state_obj = state
        return render_template('9-states.html', state=state_obj)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
