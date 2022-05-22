# Python3 code to demonstrate working of
# Dictionary with maximum keys
# Using loop + len()

# initializing list
test_list = [{"gfg": 2, "best" : 4},
			{"gfg": 2, "is" : 3, "best" : 4},
			{"gfg": 2}]

# printing original list
print("The original list is : " + str(test_list))

res = {}
max_len = 0
for ele in test_list:
	
	# checking for lengths
	if len(ele) > max_len:
		res = ele
		max_len = len(ele)
		
# printing results
print("Maximum keys Dictionary : " + str(res))
