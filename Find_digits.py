#! /usr/bin/env/ python

import sys

def remove_zero(digits):
    answer = []
    for digit in digits:
        if digit != 0:
            answer.append(digit)
    return answer

sum = 0
number = sys.stdin.readline() # Reads the input, i.e. T
number = number.rstrip() # Strips number of /n

number = int(number)

digits = list(map(int, str(number)))

new_digits = remove_zero(digits)

for digit in new_digits:
	if number % digit == 0:
            sum += 1
        else:
            continue

print sum