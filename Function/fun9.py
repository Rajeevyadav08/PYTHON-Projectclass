# Python program to Find the Number
# Occurring Odd Number of Times
# using Lambda expression and reduce function

from functools import reduce

def oddTimes(input):
	# write lambda expression and apply
	# reduce function over input list
	# until single value is left
	# expression reduces value of a ^ b into single value
	# a starts from 0 and b from 1
	# ((((((1 ^ 2)^3)^2)^3)^1)^3)
	print (reduce(lambda a, b: a ^ b, input))

# Driver program
if __name__ == "__main__":
	input = [1, 2, 3, 2, 3, 1, 3]
	oddTimes(input)
