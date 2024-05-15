#!/usr/bin/python3
""" This module creates a User class, A subclass of BaseModel """

from models.base_model import BaseModel

class State(BaseModel):
    """ This a Class for manging state objects, Subclass of BaseModel
    Public class attribute:
    name: (str)
    """

    name = ""
