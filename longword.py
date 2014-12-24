x = "what is the longest word in this sentence"

def longest_sentence(x):
	n = x.split()
	length = len(n)
	n = sorted(n, key=len)
	print n[length-1]
	
longest_sentence(x)


