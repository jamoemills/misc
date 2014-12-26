#!\usr\env\python

# -*- coding: utf-8 -*-

import sys

def tree_height(cycle, cycles, height):

    while cycle != cycles:

		if cycle % 2 == 0: # Checks if summer cycle
			height = height * 2

		elif cycle % 2 == 1: # Checks if spring cycle
			height = height + 1

		cycle += 1 

		tree_height(cycle, cycles, height)

    return height


tests = sys.stdin.readline() # Reads in the number of tests

for test in range(int(tests)): # Takes each test in turn
    
    cycles = sys.stdin.readline() # Reads in the test value
    cycles = int(cycles)

    height = 1
    cycle = 0

    final_height = tree_height(cycle, cycles, height)

    print final_height