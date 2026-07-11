'''
	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
	What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from 1 to 20?
'''

import math

def evenly_divisible():
	ans = math.lcm(*range(1,21))
	return str(ans)

print(evenly_divisible())