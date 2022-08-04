#!/usr/bin/env python3

import uuid
from datetime import datetime as dt
import models


class BaseModel:
    """defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Constructor for BaseModel

        Attributes:
            id (str): a uuid for each instance
            created_at (datetime): current datetime when instance was created
            updated_at (datetime): datetime when updated

        adds new object to `FileStorage`
        """
        if kwargs is not None and len(kwargs) > 0:
            for key in kwargs:
                self.__dict__[key] = kwargs[key]

            self.created_at = dt.fromisoformat(self.created_at)
            self.updated_at = dt.fromisoformat(self.updated_at)
            self.__dict__.pop('__class__')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """updates `updated_at` with current datetime

        saves object to file through `FileStorage` save
        """
        self.updated_at = dt.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of object

        Attr:
            dict_repr (dict): dictionary representation of object
        """
        dict_repr = dict.copy(self.__dict__)
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = dict_repr["created_at"].\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_repr["updated_at"] = dict_repr["updated_at"].\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dict_repr

    def __str__(self):
        """Overrides `__str__` method of the superclass
        """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))
