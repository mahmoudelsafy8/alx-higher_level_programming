#!/usr/bin/python3
'''
Write a class Student
'''
class Student:
    '''
    representation of a Student
    '''
    def __init__(self, first_name, last_name, age):
        '''
        defines a student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_jason(self):
        return self.__dict__
