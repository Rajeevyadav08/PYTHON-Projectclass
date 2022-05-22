import numpy as np

# We are creating an array contains n elements
# for getting first 'n' Fibonacci numbers
fNumber = int(input("Enter the value of n + 1'th number : "))
a = np.arange(1, fNumber)
length_a = len(a)

# splitting of terms for easiness
sqrt_five = np.sqrt(5)
alpha = (1 + sqrt_five) / 2
beta = (1 - sqrt_five) / 2

# Implementation of formula
# np.rint is used for rounding off to integer
Fn = np.rint(((alpha ** a) - (beta ** a)) / (sqrt_five))
print("The first {} numbers of Fibonacci series are {} . ".format(length_a, Fn))
