#!/usr/bin/python3
""" this module runs a sinple flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)

@app.teardown_appcontext
def remove_session(exception=None):
    """ removes the datavase session """
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False,
           methods=['GET'])
def hbnb_filters():
    """ hbnb filter route """
    s_query = storage.all(State)
    a_query = storage.all(Amenity)
    states = []
    amenities = []
    for state in s_query.values():
        states.append(state)
    for amenity in a_query.values():
        amenities.append(amenity)
    data = {
        "states": states,
        "amenities": amenities
    }
    return render_template('10-hbnb_filters.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
