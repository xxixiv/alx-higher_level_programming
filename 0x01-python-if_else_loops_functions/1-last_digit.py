#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = ((number * -1) % 10) * -1
noti = f"Last digit of {number} is {lastDigit}"
if lastDigit > 5:
    print(f"{noti} and is greater than 5")
elif lastDigit == 0:
    print(f"{noti} and is 0")
elif lastDigit != 0 < 6:
    print(f"{noti} and is less than 6 and not 0")
