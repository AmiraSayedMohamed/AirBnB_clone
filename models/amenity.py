#!/usr/bin/python3
"""
This module created an Amentiy class , a sybclass of BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class for managing amenity objects, subclass of BaseModel
    Public class attribute:
    name: (str)
    """
    name = ""
