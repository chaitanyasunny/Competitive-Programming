# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	a = str(digit) [::-1]
	try:
		if a[k] in "0123456789":
			return int(a[k])
		else:
			return 0
	except:
		return 0


# Done

# agsdjkgaJSFbb