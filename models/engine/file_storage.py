#!/usr/bin/python3
""" 
Module for FileStorage class 
AirBnB cone project
"""
import datetime
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    class for storing and retrieving data
    Class Methods:
        all: Returns the object
        new: updates the dictionary id
        save: Convert Python objects into JSON strings
        reload: Convert JSON string into Python objects
    Class Attributes:
    __file_path (str): Name of file to save Objects to 
    __objects (dict): Dictionary of instantiated objects
    class_dict (dict): Dictionry of all the classes
    """
    _file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}
    
    
