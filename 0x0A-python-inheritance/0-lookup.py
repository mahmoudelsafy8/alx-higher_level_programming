#!/usr/bin/python3
'''Module for lookup method.'''
def lookup(obj):
    '''looks up object attributes and methods.
    Args:
    obj (object): object to list.
    Returns:
    list: list of attributes.
    '''
    return (dir(obj))
