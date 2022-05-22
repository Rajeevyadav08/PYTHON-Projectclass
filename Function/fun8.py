def power(N, P):
    
	# if power is 0 then return 1
	# if condition is true
	# only then it will enter it,
	# otherwise not
	if P == 0: # base condition
		return 1

	# recurence relation
	return (N*power(N, P-1))

# Driver program
N = 5
P = 0

print(power(N, P))
