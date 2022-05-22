# Python3 code to demonstrate working of
# Factors Frequency Dictionary
# Using loop

# initializing list
test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]

# printing original list
print("The original list : " + str(test_list))

res = dict()

# iterating till max element
for idx in range(1, max(test_list)):
	res[idx] = 0
	for key in test_list:
		
		# checking for factor
		if key % idx == 0:
			res[idx] += 1
		
# printing result
print("The constructed dictionary : " + str(res))
