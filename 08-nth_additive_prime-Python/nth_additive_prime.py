# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

primes = []
nonprimes =[]
def is_prime(n):
	if n < 1 or n % 1 > 0:
		return 0

	for i in range(2,n//2):
		if n % i == 0:
			print("non prime")
			return False
		else:
			print("prime")
			return True
			break

def prime_list():
	for i in range(2,100):
		if is_prime(i) == True:
			primes.append(i)
		else:
			nonprimes.append(i)

def is_additiveprime():
	pass

def fun_nth_additive_prime(n):
	return 1



is_prime(2)


print("primes:")
print(primes)
print("nonprimes:")
print(nonprimes)
