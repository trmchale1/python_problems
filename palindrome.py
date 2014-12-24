palindrome = raw_input()
def nailin_pailin(palindrome):
	palindrome_len = len(palindrome)
	if palindrome_len == 0:
		print True 
		return
	elif  palindrome_len == 1:
		print True
		return
	print palindrome[0]
	print palindrome[palindrome_len-1]
	if palindrome[0] != palindrome[palindrome_len-1]:
		print False
		return
	palindrome = palindrome[1:palindrome_len-1]
	print palindrome
	nailin_pailin(palindrome)

x = nailin_pailin(palindrome)
