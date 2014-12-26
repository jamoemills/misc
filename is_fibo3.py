#!/usr/bin/python

# -*- coding: utf 8 -*-

import sys

def fibo():

	new_fib = fibo_seq[-1] + fibo_seq[-2]
	return new_fib

tests = sys.stdin.readline()
tests = int(tests)

for test in range(tests):
    
    number = sys.stdin.readline()
    number = int(number)

    fibo_seq = [0, 1] # First elements in sequence

    while number > fibo_seq[-1]: # Only generates relevant fibo numbers for the number 
        fibo_seq.append(fibo())

    if number in fibo_seq:
        print 'IsFibo'
    else: 
        print 'IsNotFibo'