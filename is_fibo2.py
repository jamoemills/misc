#!/usr/bin/python

# -*- coding: utf 8 -*-

import sys

def fibo(n): # Creates fibonacci sequence

	if (n == 0):
		return 0

	elif (n == 1):
		return 1

	else:
		return fibo(n-1) + fibo(n-2)

tests = sys.stdin.readline()

for test in tests:

	fibo_seq = [0, 1] # First elements in sequence
	
	number = int(test)

	n = 2

	while number > fibo_seq[-1]: # Only generates relevant fibo numbers for the number 
		fibo_seq.append(fibo(n))
		n += 1

	if number in fibo_seq:
		print 'isFibo'
	else: 
		print 'isNotFibo'