#!\usr\env\python

import sys

tests = int(sys.stdin.readline())

for test in range(tests):
    cycles = int(sys.stdin.readline())
    height = 1

    for cycle in range(cycles):
        if cycle % 2 == 0:
            height *= 2
        else:
            height += 1

    print(height)