x = 3

def recur_sum(x):
	if x == 0: 
		return 0
	return x + recur_sum(x-1)

n = recur_sum(x)
print n
