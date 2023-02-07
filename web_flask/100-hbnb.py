#!/usr/bin/python3
""" this module runs a sinple flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User


app = Flask(__name__)

@app.teardown_appcontext
def remove_session(exception=None):
    """ removes the datavase session """
    storage.close()

@app.route('/hbnb', strict_slashes=False,
           methods=['GET'])
def hbnb():
    """ hbnb filter route """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places_q = storage.all(Place)
    users = storage.all(User)
    places = []
    for place in places_q.values():
        id = place.user_id
        for user in users.values():
            if user.id == id and user.id is not None:
                place.owner = user.last_name + " " + user.first_name
                break
        places.append(place)
    data = {
        "states": states.values(),
        "amenities": amenities.values(),
        "places": places
    }
    return render_template('100-hbnb.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
