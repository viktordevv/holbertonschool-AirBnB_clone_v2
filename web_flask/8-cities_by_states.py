#!/usr/bin/python3
""" 
Script that starts a Flask web application 
"""

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """cities_by_states
    Function that displays a HTML page with a list of all
    State objects from a database
    """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """teardown_db
    Function that removes the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
