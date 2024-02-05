#!/usr/bin/python3
'''Module for is_same_class mathod'''
def is_same_class(obj, a_class):
    '''Determines if object is exactly instance of a class'''
    return type(obj) == a_class
