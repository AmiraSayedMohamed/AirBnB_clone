#!/usr/bin/python3

""" This module creates a Review class, a subclass of BaseModel """

from models.base_model import BaseModel

class Review(BaseModel):
    """ A Class for managing review objects, subclass of BaseModel
    Public class attributes:
    place_id: (str)
    user_id: (str)
    text: (str)
    """

    place_id = ""
    user_id = ""
    text = ""
