#!/usr/bin/python
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print(f"{number} is positive\n")
elif number < 0:
    print(f"{number} is negative\n")
else:
    print(f"{number} is zero\n")
