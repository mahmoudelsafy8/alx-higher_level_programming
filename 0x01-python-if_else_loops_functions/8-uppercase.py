#!/usr/bin/python3
def islower(i):
    if ord(i) >= 97 and ord(i) <= 122:
        return (ord(i) - 32)
    else:
        return ord(i)

def uppercase(str):
    str_n = ""
    for i in str:
        str_n += "%c" % islower(i)
        print("{:s}".format(str_n))
