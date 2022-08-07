#!/usr/bin/env python3

import cmd
import json
from models.base_model import BaseModel
import models
from models.mapper import mapper

storage = models.storage
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    file = None

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

        if arg in mapper:
            model = mapper[arg]
            new_model = model()
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
        
        all_objects = storage.all()
        instances_list = list()

        if len(argv[0]) == 0:
            for key in all_objects:
                instances_list.append(str(all_objects[key]))

            print(instances_list)

        elif argv[0] in mapper:
            for key in all_objects:
                if key.startswith(argv[0]):
                    instances_list.append(str(all_objects[key]))

            print(instances_list)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        key = self._check_class_and_id(arg)
        update_dict = self._check_attribute_name_and_value(arg)

        all_objects = storage.all()

        if key is not None and update_dict is not None:
            obj = all_objects[key]

            for attr in update_dict:
                setattr(obj, attr, update_dict[attr])
            obj.save()

    # ------- utility functions ----------
    def _check_class_and_id(self, arg):
        "Error checker for class and id in arguements"
        argv = arg.split(" ")

        if len(argv[0]) == 0:
            print("** class name missing **")

        elif argv[0] not in mapper:
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

    def default(self, line):
        argv = line.split(".")

        if len(argv) == 1:
            super().default(line)

        elif argv[1] == "all()":
            self.do_all(argv[0])

        elif argv[1].startswith("show"):
            obj_id = argv[1].split("(")[1].strip(")").strip("'\"")
            arg = f"{argv[0]} {obj_id}"
            self.do_show(arg)
        elif argv[1].startswith("destroy"):
            obj_id = argv[1].split("(")[1].strip(")").strip("'\"")
            arg = f"{argv[0]} {obj_id}"
            self.do_destroy(arg)
        elif argv[1].startswith("update"):
            update_info = argv[1].split('", "')
            obj_id = update_info[0].split('("')[1]
            attr_name = update_info[1].strip()
            attr_value = update_info[2].strip('")')
            arg = f"{argv[0]} {obj_id} {attr_name} {attr_value}"
            self.do_update(arg)

    def _check_attribute_name_and_value(self, arg):
        "Error checker for attribute name and value"
        argv = arg.split(" ")

        #TODO: keep as one string if its starts with double quotes

        if len(argv) == 2:
            print("** attribute name missing **")

        elif len(argv) == 3:
            print("** value missing **")

        else:
            return {argv[2]: argv[3].strip('"\'')}

        return None


if __name__ == "__main__":
    HBNBCommand().cmdloop()
