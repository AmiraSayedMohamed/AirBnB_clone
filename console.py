#!/usr/bin/python3
"""
Module for the entry point of the command interpreter
Defines the HBnB console
"""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split
from models import storage
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

    prompt = "(hbnb)"

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
        """ Command to Exit form the programm """
        sys.exit(0)
    
    def do_EOF(self, line):
        """ Exit form the program(console) """
        sys.exit(0)
    
    def emptyline(self):
        """ Overwritint the empty lines,  Ignore empty spaces """
        return False

    def do_create(self, line):
        """" Create < class > a new instances of a class < key 1>= < value 2> with given keys/values and prints it's id"""
        # Check if the input line is empty
         if not line:
             raise SyntaxError()

         else:
             # Split the input line into the class name and the rest of the aruments
             components = line.split(" ", 1)
             class_name = components[0]
             
             #check if there are key-value pairs provided
             if len(components) == 1:
                 kwargs_string = ""
             else:
                 kwargs_string = compoents[1]

             try:
                 # Retriev the class from the global namespace
                 cls = globals().get(class_name)
                 if cls is None:
                     raise NameError()  # Rais name error if the class does not exist
                 kwargs = {}
                 if kwargs_String:
                     # Spint the key - value pairs
                     pairs = kwargs_string.split(" ")
                     for pair in pairs:
                         key, value = pair.split("=", 1)
                         # Handle string values enclosed in double quotes
                         if value.startswith('"') and value.endswith('"'):
                             value = value[1:-1].replace("_", " ")
                         else:
                             # Try to evaluate the value as a Python expressioin
                             try:
                                 value = eval(value)
                             except Exeption:
                                 continue
                         kwargs[key] = value
                 
                 # Crete an instance of the class with the provided key-vlaue pairs
                 obj = cls(**kwargs)
                 storage.new(obj)  # Add the objects to storage
                 obj.save() # Save the objects
                 print(obj.id)  # Print the ID of the newly created object

             except SyntaxError:
                 print("** class name missing **") # Print error if class name is missing
             except NameError:
                 print("** class doesn't exist **") # Print error if class doesn't exist 
             except Exception as e:
                print(f"** error: {e} **") # Print any other errors that occur

    def do_show(self, line):
        """ Prints the string representaion of an instance with given class name and id """
        if not line:
            print("** class name missing **")
            return

        parts = line.split()

        if len(parts) < 1:
            print("** class name missing **")
            return
        
        class_name = parts[0]

        if class_name not in self.__classes_:
            print("** class doesn't exist **")
            return
         
        if len(parts) < 2:
            print("** instance id missing **")
            return

        instance_id = parts[1]
        object_key = f"{class_name}.{instance_id}"

        try:
            obj = storage.all()[object_key]
            print(obj)
        except KeyError:
            print("** no instance found **")

    
    def do_destroy(self, line):
        """ Deleted an instance based on the class name and id """

        # Checks if the input line is empty
        if not line:
            print("** class name missing **")
            return

        # Split the input line into parts
        parts = line.split()

        # Validate the class name 
        if len(parts) < 1:
            print("** class name missing **")
            return

        class_name = parts[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return

        # Validate the instance ID
        if len(parts) < 2:
            print("** instance is missing **")
            return

        instance_id = parts[1]
        object_key = f"{class_name}.{instanct_id}"

        # Retrieve all objects from storage
        objects = storage.all()

        # Check if the objects exists and delete it 
        if object_key in objects:
            del objects[object_key]
            storage.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
