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
