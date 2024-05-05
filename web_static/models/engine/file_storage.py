#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """File-based storage.

    Attributes:
        __file_path: Path to the JSON file.
        __objects: Dictionary of stored objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Get all objects or specific class objects.

        Args:
            cls (class, optional): Class to filter.

        Returns:
            dict: Retrieved objects.
        """

        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            cls_dict = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    cls_dict[key] = obj
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary.
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serialize the storage dictionary to a JSON file."""
        serialized_objs = {key: obj.to_dict()
                           for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserialize the JSON file to populate the storage dictionary."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    self.__objects[key] = cls(**obj_data)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete an object from the storage dictionary.

        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Reload data from file."""
        self.reload()
