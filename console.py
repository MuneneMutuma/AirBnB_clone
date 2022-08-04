#!/usr/bin/env python3

import cmd
import json
from models.base_model import BaseModel
import models


storage = models.storage
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    file = None
    __cls_list = ["BaseModel"]

    #------ 6. Console 0.0.1 ------
    def emptyline(self):
        'does nothing when an empty line is passed. asks for new prompt'
        pass

    def do_quit(self, arg):
        'Exit the cmd'
        exit()
    
    def do_EOF(self, arg):
        'Exit the cmd'
        exit()

    # --------- 7. Console 0.1 ----------
    def do_create(self, arg):
        "creates a new instance of BaseModel and saves it to JSON file"

        if arg == "BaseModel":
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)
        elif len(arg) > 0:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints string representation of and instance based on class name and id"""
        key = self._check_class_and_id(arg)
        all_objects = storage.all()
        if key is not None:
            print(all_objects[key])

    def do_destroy(self, arg):
        "Deletes instance based on class name and id and saves to json file"
        key = self._check_class_and_id(arg)
        all_objects = storage.all()
        if key is not None:
            all_objects.pop(key)
            storage.save()

    def do_all(self, arg):
        "prints all string representation of all instances based or not on the class name"
        argv = arg.split(" ")
        cls_list = HBNBCommand.__cls_list
        
        all_objects = storage.all()
        instances_list = list()
        if len(argv[0]) == 0:
            for key in all_objects:
                instances_list.append(all_objects[key])

            print(instances_list)
        elif argv[0] in cls_list:
            for key in all_objects:
                if key.startswith(argv[0]):
                    instances_list.append(all_objects[key])

            print(instances_list)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        key = self._check_class_and_id(arg)
        update_dict = self._check_attribute_name_and_value(arg)
        all_objects = storage.all_dict()

        obj_dict = all_objects[key]

        obj_dict[update_dict["attribute"]] = update_dict["value"]
        storage.save()


    # ------- utility functions ----------
    def _check_class_and_id(self, arg):
        "Error checker for class and id in arguements"
        cls_list = HBNBCommand.__cls_list
        argv = arg.split(" ")

        if len(argv[0]) == 0:
            print("** class name missing **")

        elif argv[0] not in cls_list:
            print("** class doesn't exist **")

        elif len(argv) == 1:
            print("** instance id missing **")

        else:
            obj_id = f"{argv[0]}.{argv[1]}"
            all_objects = storage.all()

            if obj_id in all_objects:
                return obj_id
            else:
                print("** no instance found **")
        return None

    def _check_attribute_name_and_value(self, arg):
        "Error checker for attribute name and value"
        argv = arg.split(" ")

        if len(argv) == 2:
            print("** attribute name missing **")

        elif len(argv) == 3:
            print("** value missing **")

        else:
            return {"attribute": argv[2], "value": argv[3].strip('"')}

        return None


if __name__ == "__main__":
    HBNBCommand().cmdloop()
