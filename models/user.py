#!/usr/bin/python3

"""This is a Modeule to Create auserclass , subclass of BaseModel"""

from models.base_model import BaseModel

class User(BaseModel):
    """ THis is a class for managing user objects subclass of The baseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
