# Python3 code to demonstrate working of
# Remove keys with substring values
# Using any() + generator expression

# initializing dictionary
test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing substrings
sub_list = ['love', 'good']

# Remove keys with substring values
# Using any() + generator expression
res = dict()
for key, val in test_dict.items():
    if not any(ele in val for ele in sub_list):
	    res[key] = val
		
# printing result
print("Filtered Dictionary : " + str(res))
