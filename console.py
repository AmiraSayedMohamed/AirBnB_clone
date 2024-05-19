#!/usr/bin/python3
"""
Module for the entry point of the command interpreter
Defines the HBnB console
"""
import cmd
import sys
from models.base_model import BaseModel
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re
import json
from datetime import datetime
import models

class HBNBCommand(cmd.Cmd):

    """
    Class for the command interpreter
    Defines the HolbrtonBNB command interpreter
    Attributes:
    prompt (str): The command prompt
    """

    prompt = "(hbnb) "

    __classes_ = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
    def default(self, line):
        """ Catchs the command if nothing else matches, 
        Default behavior for cmd module when input in invalid"""
        self._precmd(line)

    def do_quit(self, line):
        """Quit command to exit the program
        """

        sys.exit(0)

    def do_EOF(self, line):
        """Quit command to exit the program
        """

        sys.exit(0)
    
    def emptyline(self):
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
