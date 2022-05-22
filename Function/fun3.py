# defined function
x = 123

def sum():
	x = 98
	print(x)
	print(globals()['x'])


# drivercode
print(x)

# assigning function
z = sum

# invoke function
z()
z()
