#!/usr/bin/python3
""" This a module creates a City class, subclass of BaseModel """
from models.base_model import BaseModel

class City(BaseModel):
    """
    Class for managing city objects, subclass of BaseModel
    Public class attributes:
    state_id: (str) will be state.id
    name: (str)
    """

    state_id = ""
    name = ""

