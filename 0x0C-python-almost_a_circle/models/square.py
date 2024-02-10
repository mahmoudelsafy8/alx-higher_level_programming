#!/usr/bin/python3
"""
Module for square class
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        method should return [Square] output
        """
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.geight = value

    def __update(self, id=None, size=None, x=None, y=None):
        """
        method that Update the class Square to assigns attributes
        """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """
        method that Update the class Square to assigns attributes
        """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
