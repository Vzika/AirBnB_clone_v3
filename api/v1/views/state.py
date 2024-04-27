#!/usr/bin/python3
"""
Index file for api.v1.views
"""
from api.v1.views import app_views
from models.state import State
from flask import jsonify, abort, make_response
from models import storage


@app_views.route('/states', strict_slashes=False)
def get_states():
    """
    return all states
    """
    return storage.all(State)


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_state(state_id):
    """
    return a state by its id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return state.to_dict()


@app_views.route('/states/<state_id>', method='DELETE', strict_slashes=False)
def delete_state(state_id):
    """
    return an empty dictinary after deleting state by id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return make_response({}, 200)
