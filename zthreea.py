zthreea = raw_input()

def find_z(zthreea):
	x = len(zthreea)
	for i in range(0,x-1,+1):
		if zthreea[i] == "a":
			if zthreea[i+1] == "z":
				return True
			elif zthreea[i+2] == "z":
				return True
			elif zthreea[i+3] == "z":
				return True

	return False

n = find_z(zthreea)
print n
