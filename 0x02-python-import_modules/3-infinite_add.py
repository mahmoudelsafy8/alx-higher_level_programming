#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add_int = 0
    for i in range(1, len(argv)):
        add_int += int(argv[i])
        print("{}".format(add_int))
