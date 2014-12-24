#! /usr/bin/env/ python

import sys

sum = 0
number = sys.stdin.readline() # Reads the input, i.e. T
number = number.rstrip() # Strips number of /n

number = int(number)

digits = list(map(int, str(number)))

for digit in digits:
    if digit in range(1-10):
        if number % digit == 0:
            sum += digit
        else:
            continue

print sum # Nothing being added to the sum