#!/usr/bin/python3
'''
Moduls for Base Class
'''
class Base:
    '''
    representation of the base
    '''
    __nb_objects = 0
    def __init__(self, id=None):
        '''
        class constructor
        '''
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = Base.__nb_objects
