# using kwargs
# in functions


def printValues(**kwargs):
	for key, value in kwargs.items():
		print("The value of {} is {}".format(key, value))


# driver code
if __name__ == '__main__':
	printValues(abbreviation="GFG", full_name="geeksforgeeks")
