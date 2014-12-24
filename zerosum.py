arr = [3,3,3,3,3,-5,-4,-3,-2,-1]

def zero_sum(arr):
	len_arr = len(arr)
	x = []
	for i in range(0, len_arr-1,+1):
		for j in range(i+1,len_arr-1,+1):
			 if arr[i] + arr[j] == 0:
				x.extend([i,j])
	return x

k = zero_sum(arr)
print k
#z = len(k)
#for n in range(0,z-1,+1):
#	print k[n]

