x = raw_input()
x = int (x)
def time_conversion(x):
	n = x % 60
	a = x / 60
	n = int (n)
	a = int (a)
	print "%d : %d" % (a,n)

time_conversion(x)
