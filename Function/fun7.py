# Iterating With Python Lambdas

# list of numbers
l1 = [4, 2, 13, 21, 5]

l2 = []

# run for loop to iterate over list
for i in l1:
	
	# lambda function to make square
	# of number
	temp=lambda i:i**2

	# save in list2
	l2.append(temp(i))

# print list
print(l2)
