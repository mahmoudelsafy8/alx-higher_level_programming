#!/usr/bin/python3
"""Module for BaseGeometry class"""
class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Metod to compute this area"""
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """Method for validator the value"""
        if type(value) != int:
            raise TypeError("{} must be an intager".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
