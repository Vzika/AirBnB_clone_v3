#!/usr/bin/python3
"""State view objects that handles all default RESTFul API actions
"""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
def states():
    """returns a list of all states
    """
    states_data = []
    for state in storage.all(State).values():
        states_data.append(state.to_dict())
    return jsonify(states_data)


@app_views.route('/states/<state_id>', strict_slashes=False)
def state(state_id):
    """returns a state object by id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return state.to_dict()


@app_views.route('/states/<state_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """deletes a state object by id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return {}, 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """creates a state object
    """
    state = request.get_json()
    if state is None:
        abort(400, "Not a JSON")
    if "name" not in state:
        abort(400, "Missing name")
    state = State(**state)
    state.save()
    return state.to_dict(), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
# def update_state(state_id):
#     """updates a state object
#     """
#     state = storage.get(State, state_id)
#     if state is None:
#         abort(404)
#     update = request.get_json()
#     if update is None:
#         abort(400, "Not a JSON")
#     for key, value in update.items():
#         if key not in ["id", "created_at", "updated_at"]:
#             setattr(state, key, value)
#     state.save()
#     return state.to_dict(), 200

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
        for k, v in body:
            setattr(state, k, v)
    except KeyError:
        pass
    storage.save()
    return (state.to_dict(), 200)
