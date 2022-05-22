# Python3 code to demonstrate working of
# Extract Key's Value, if Key Present in List and Dictionary
# Using all() + list comprehension

# initializing list
test_list = ["Gfg", "is", "Good", "for", "Geeks"]

# initializing Dictionary
test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

# initializing K
K = "Gfg"

# printing original list and Dictionary
print("The original list : " + str(test_list))
print("The original Dictionary : " + str(test_dict))

# using all() to check for occurrence in list and dict
# encapsulating list and dictionary keys in list
res = None
if all(K in sub for sub in [test_dict, test_list]):
	res = test_dict[K]

# printing result
print("Extracted Value : " + str(res))
