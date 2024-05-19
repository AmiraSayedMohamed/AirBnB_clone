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
    __file_path = "file.json"
    __objects = {}
    classes_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}
    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ set new __objects to existing dictionary of instances """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Save of Serialize __objects to json file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """ Reload the stored objects , converto obj back to instance """
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:

            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes

