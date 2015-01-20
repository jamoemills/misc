#!/usr/bin/env python

import sys

max = 0

# get input
_l = int(sys.stdin.readline().rstrip())
_r = int(sys.stdin.readline().rstrip())
l_number = min(_l, _r)
r_number = max(_l, _r)

# get permutations
for a in range(l_number, r_number+1):
    for b in range(a, r_number+1):
        # find max XOR
        if (a^b > max):
            max = a^b
            
print max
