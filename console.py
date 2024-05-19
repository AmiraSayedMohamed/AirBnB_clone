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
from models import storage

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
                 if kwargs_string:
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

        """ Catchs the command if nothing else matches, 
        Default behavior for cmd module when input in invalid"""
        self._precmd(line)
    def do_all(self, line):
        """ Display string representaion of all instances of a given class"""

        # Check if the input line is empty
        if not line:
            # If no class is specified , display all instantiated objects
            objects = storage.all()
            print([str(obj) for obj in objects.values()])
            return

        try:
            args = line.split(" ")
            class_name = args[0]


            if class_name not in self.__classes_:
                raise NameError("** class doesn't exist **")

            # Display string representaion of instances of the specified class
            objects = storage.all()
            print([str(obj) for obj in objects.values() if obj.to_dict()["__class__"] == class_name])

        except NameError as e:
            print(e)

    def do_update(self, line):
        """ Updattes an instance by adding or updatint attribute """

        # check if the input line is empty
        if not line:
            print("** class name missing **")
            return
        try: 
            # Split the input into parts
            args = line.split(" ")

            # Validate class name
            if len(args) < 1:
                raise SyntaxError("** class name missing **")
            class_name = args[0]

            if class_name not in HBNBCommand.__classes_:
                raise NameError("**class doesn't exist **")
            # Validate instance ID
            if len(args) < 2:
                raise IndexError("** instance is missing **")
            
            instance_id = args[1]
            object_key = f"{class_name}.{instance_id}"

            objects = storage.all()

            # Check if the instance exists 
            if object_key not in objects:
                raise KeyError("** no instance found **")

            # Validate attribute name 
            if len(args) < 3:
                raise AttributeError("** attribute name missing **")
            
            attribute_name = args[2]

            #Validate attribute value
            if len(args) < 4:
                raise ValueError("** value missing **")

            attribute_value = args[3]

            # Update the attribute of the instance 
            setattr(objects[object_key], attribute_name, attribute_value)
            storage.save()
        
        except (SyntaxError, NameError, IndexError, KeyError, AttributeError, ValueError) as e:
            print(e)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
