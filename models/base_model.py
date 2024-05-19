#!/usr/bin/python3

""" This script is the base model ,
Parent class to all classes in the AirBnb clone project """

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    This is a class from which all other classes will inherit

    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save__(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """ Initializes instance attributes: uuid4, dates created/updated
        Args:
            - *args: list of The  arguments
            - **kwargs: dictionary of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if "created_at" == key:
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns official string representaion, class name, id, and dictionary
        """

        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        Instance method to:
        - update current datetime
        - invoke function save ()
        - save to the  serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __repr__(self):
        """
        A function that returns string repr
        """
        return (self.__str__())

    def to_dict(self):
        """
        Function returns a dictionary containig
        all keys/ values with string format of times
        """
        my_dictionary = self.__dict__.copy()
        my_dictionary["__class__"] = type(self).__name__
        my_dictionary["created_at"] = my_dictionary["created_at"].isoformat()
        my_dictionary["updated_at"] = my_dictionary["updated_at"].isoformat()
        return my_dictionary
