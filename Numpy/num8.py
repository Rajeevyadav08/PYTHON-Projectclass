import numpy as np

an_array = np.array([[1, 2], [3, 4]])
another_array = np.array([[1, 2], [3, 4]])

comparison = an_array == another_array
equal_arrays = comparison.all()

print(equal_arrays)
