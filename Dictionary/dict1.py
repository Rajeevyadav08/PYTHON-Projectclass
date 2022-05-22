def merge(dict1, dict2):
    res = dict1 | dict2
    return res

dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = merge(dict1, dict2)
print(dict3)