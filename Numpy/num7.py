import numpy as np


x = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
print("Original array:")
print(x)

print("Most frequent value in above array")
y = np.bincount(x)
maximum = max(y)

for i in range(len(y)):
	if y[i] == maximum:
		print(i, end=" ")
