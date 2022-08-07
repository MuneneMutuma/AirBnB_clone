#!/usr/bin/env python3
"""File Storage module

This module handles serialization of `BaseModel` objects
and its subclasses from and to json, and saving it to json file
"""
import json
import ast
from datetime import datetime as dt


class FileStorage:
    """FileStorage Module

    Methods:
        all: returns all objects in the file
        new(obj): adds a new object to the file storage
        save: saves `FileStorage` objects to json file
        reload: serializes json file to objects and stores it in FileStorage
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """Returns all objects in file storage
        """
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to file storage
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves file storage objects to json file

        Serializes object to json format and then saves to the file
        """
        objects_json = dict()

        for obj in FileStorage.__objects:
            objects_json[obj] = FileStorage.__objects[obj].to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_json, f)

    def reload(self):
        """Reloads objects from json file to file storage
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = f.read()
                objects_dict = json.loads(data)
                from models.mapper import mapper
                for obj in objects_dict:
                    cls = mapper[obj.split(".")[0]]
                    FileStorage.__objects[obj] = cls(**objects_dict[obj])
        except FileNotFoundError:
            pass
