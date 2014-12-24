x = "foughettaboutit"
count = 0
def count_vowels(x, count):
	a = len(x)
		
	for i in range(0,a,+1):
		print x[i]

		if x[i] == "a":
			count = count + 1
		if x[i] == 'e': 
			count = count + 1
		if x[i] == 'i': 
			count = count + 1
		if x[i] == 'o':
			count = count + 1
		if x[i] == 'u':
			count = count + 1
	print count

count_vowels(x,count)
