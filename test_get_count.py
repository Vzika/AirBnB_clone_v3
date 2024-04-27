#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

my_state = State("Rivers")
storage.new(my_state)
my_state = State("Osun")
storage.new(my_state)
print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))
# print("States".format(storage.all(State)))
# first_state_id = list(storage.all(State).values())[0].id
# print("First state: {}".format(storage.get(State, first_state_id)))