#!/usr/bin/python3
'''Module for lookup method.'''

def lookup(obj):
    '''
    look up object attributes and method.
    Args:
    obj (object): object list.
    Returns:
    list: list of attributes.
    '''
    return dir(obj)
