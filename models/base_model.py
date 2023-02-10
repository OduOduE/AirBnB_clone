#!/usr/bin/python3
"""
A module BaseModel that defines common attributes/methods for other classes
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ A class that defines common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Instantiation of the class """

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Returns the string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Updates 'self.updated_at' with the current datetime """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary:
        - only instance attributes will be returned
        - a key __class__ is added to class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = slef.__dict__[k].isoformat()
                dict_1 = v
        return dict_1
