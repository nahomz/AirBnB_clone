#!/usr/bin/python3
"""this module contains the FileStorage Class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State

classes = {"BaseModel": BaseModel, "User": User, "City": City, "Place": Place,
           "Amenity": Amenity, "Review": Review, "State": State}


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances
    """

    __file_path = "file.json"  # str - path to the JSON file
    __objects = {}  # stores all objects by <class_name>.id

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects with key <obj class_name>.id"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        serializes the __objects and saves to the JSON file using
        path: __file_path)
        """

        new_json = {}
        for key in self.__objects:
            new_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as myFile:
            json.dump(new_json, myFile)

    def reload(self):
        """
        deserializes the JSON file to __objects only if file exists
        """
        try:
            with open(self.__file_path, encoding="UTF-8") as myFile:
                json_obj = json.load(myFile)
            for key, value in json_obj.items():
                name = classes[value["__class__"]](**value)
                self.__objects[key] = name
        except FileNotFoundError:
            pass
