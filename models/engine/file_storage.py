#!/usr/bin/env python3

import json
import models
import ast
from datetime import datetime as dt

def json_serializer(obj):
    """JDON Drializer for objects not serializable by default json code"""

    if isinstance(obj, dt):
        print(type(obj))
        return obj.isoformat()

class FileStorage:

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        all_dict = dict()

        for key in FileStorage.__objects:
            obj_dict = FileStorage.__objects[key]
            all_dict[key] = self.__dict_to_str(obj_dict)

        return all_dict

    def new(self, obj):
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)


    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = f.read()
                FileStorage.__objects = json.loads(data)
        except FileNotFoundError:
            pass

    def __dict_to_str(self, obj_dict):
        tmp = dict.copy(obj_dict)

        class_name = tmp.pop("__class__")

        tmp["created_at"] = dt.fromisoformat(tmp["created_at"])
        tmp["updated_at"] = dt.fromisoformat(tmp["updated_at"])

        return f"[{class_name}] ({tmp['id']}) {tmp}"

    def all_dict(self):
        return FileStorage.__objects
