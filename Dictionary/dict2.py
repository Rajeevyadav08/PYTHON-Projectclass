test_dict = {'Gfg' : 4, 'is' : 5, 'best' : 9} 
test_list = [8, 3, 2]
  
# printing original dictionary and list
print("The original dictionary is : " + str(test_dict))
print("The original list is : " + str(test_list))
  
# zip() and dictionary comprehension mapped in one liner to solve
res = {idx: {key : test_dict[key]} for idx, key in zip(test_list, test_dict)}
          
# printing result 
print("The mapped dictionary : " + str(res)) 
