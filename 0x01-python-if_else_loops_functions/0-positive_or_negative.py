#!/usr/bin/python3
import random
number = random.ranint(-10,10)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negaive".format(number))