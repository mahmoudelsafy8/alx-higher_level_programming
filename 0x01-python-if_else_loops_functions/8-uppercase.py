#!/usr/bin/python3
def islower(i):
    if ord(i) >= ord('a') and ord(i) <= ord('z'):
        return True
    else:
        return False

def uppercase(str):
    for i in str:
        print("{:i}"
                .format(ord(i) if not islowr(i) else ord(i) - 32),
                end='')
        print("")