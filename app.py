#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    last = -(-number % 10)
print(f"Last digit of {number} is {last}")