#!\usr\bin\python
# -*- coding: utf-8 -*-

import sys

def  maxXor( l,  r):
	Xor_values = []
	x = r - l
	while x != 0:
		for i in range(l + x, r + 1): # O(n**2)
		  	Xor = (l + x) ^ i
		  	Xor_values.append(Xor)
	  	x -= 1
	return max(Xor_values)

_l = sys.stdin.readline()
_r = sys.stdin.readline()

_l = int(_l)
_r = int(_r)

res = maxXor(_l, _r);
print(res)