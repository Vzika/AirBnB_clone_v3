#!/usr/bin/python3
"""
Index file for api.v1.views
"""
from api.v1.views import app_views
from models.state import State
from flask import jsonify, abort, make_response, request
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


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """
    return an empty dictinary after deleting state by id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    return make_response({}, 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """
    return a new State with the status code 201
    """
    if not request.get_json():
        abort(400, "Not a JSON")
    if "name" not in request.get_json():
        abort(400, "Missing name")
    new_state = State(**(request.get_json()))
    storage.new(new_state)
    storage.save()
    return make_response(new_state.to_dict(), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """
    return an updated dictinary by id
    """
    state = storage.get(State, state_id)
    body = request.get_json()
    try:
        body.pop('id')
        body.pop('created_at')
        body.pop('update_at')
    except KeyError:
        pass
    storage.save()
    return make_response(state.to_dict(), 200)
