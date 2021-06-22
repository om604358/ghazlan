import math


primes = []
def primeFactors(n):
	
	while n % 2 == 0:
		primes.append(2)
		n = n / 2

	for i in range(3,int(math.sqrt(n))+1,2):
		while n % i== 0:
			primes.append(i)
			n = n / i

	if n > 2:
		primes.append(n)
		
n = 10**5
primeFactors(n)
not_deblocated_primes = [i for j, i in enumerate(primes) if i not in primes[:j]] 
print([[i,primes.count(i)] for i in not_deblocated_primes])
