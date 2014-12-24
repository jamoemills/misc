#!\usr\env\bin\ python

import sys

def create_fib_sequence():

	fib_sequence = [0, 1]
	max_N = 10**10
    
	while fib_sequence[-1] < max_N:

		new_fib = fib_sequence[-1] + fib_sequence[-2]
		fib_sequence.append(new_fib)
        
	return fib_sequence

tests = int(sys.stdin.readline())

for test in range(tests):

    fib_sequence = create_fib_sequence()

    number = sys.stdin.readline()
    number = number.strip()
    number = int(number)

    if number in fib_sequence:
        print 'IsFibo'
    else:
        print 'IsNotFibo'