#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lastNumber = int(repr(number)[-1])
position = ""
if number < 0:
    lastNumber = -lastNumber
if lastNumber > 5:
    position = "and is greater than 5"
elif lastNumber < 6 and lastNumber != 0:
    position = "and is less than 6 and not 0"
else:
    position = "and is 0"
print(f"Last digit of {number} is {lastNumber} {position}")
