#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objs = {}
        if cls:
            class_name = cls.__name__
            for key, val in self.__objects.items():
                # print(val.__class__.__name__, class_name)
                if val.__class__.__name__ == class_name:
                    objs[key] = val
            return objs
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    # print(classes[val['__class__']](**val))
                    self.all()[key] = eval(val["__class__"])(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it's inside"""
        if obj:
            class_name = f"{obj.__class__.__name__}.{obj.id}"
            del FileStorage.__objects[class_name]

    def close(self):
        """Close the session"""
        self.reload()
