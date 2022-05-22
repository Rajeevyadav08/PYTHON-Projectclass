# Python3 code to demonstrate working of 
# Reverse Dictionary Keys Order
# Using reversed() + items()
  
# initializing dictionary
test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}
  
# printing original dictionary
print("The original dictionary : " + str(test_dict))
  
# Reverse Dictionary Keys Order
# Using reversed() + items()
res = dict(reversed(list(test_dict.items())))
  
# printing result 
print("The reversed order dictionary : " + str(res)) 