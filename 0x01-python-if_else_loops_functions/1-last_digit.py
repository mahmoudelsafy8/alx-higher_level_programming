#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = -(ld)
the_str = ("Last digit of {} is {}".format(number, ld))
if ld > 5:
    print(f"{ld} and is greater than 5")
else ld == 0:
    print(f"{ld} and is 0")
else ld < 6:
    print(f"{ld} and is less than 6 and not 0")
