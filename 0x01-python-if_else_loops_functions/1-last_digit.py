#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
y = number

if number < 0:
    negative = True
    number = abs(number)
else:
    negative = False

while number >= 10:
    number %= 10

if negative is True:
    number *= -1

if number == 0:
    print(f"Last digit of {y:d} is {number:d} and is 0")
elif number > 5:
    print(f"Last digit of {y:d} is {number:d} and is greater than 5")
else:
    print(f"Last digit of {y:d} is {number:d} and is less than 6 and not 0")
