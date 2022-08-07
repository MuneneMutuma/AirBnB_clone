#!/usr/bin/env python3

import json
import ast
from datetime import datetime as dt

class FileStorage:

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        objects_json = dict()

        for obj in FileStorage.__objects:
            objects_json[obj] = FileStorage.__objects[obj].to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_json, f)

    def reload(self):
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
