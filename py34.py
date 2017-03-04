# Mersenne prime
import math
def isPrime(num):
	for i in range(2,int(math.sqrt(num))+1):
		if num%i==0:
			return False
	return True
def mersennePrime(num):
	if isPrime(num):
		return True
	else:	
		return False
start=input()
end=input()
liz=[]
for i in range(start,end):
	if mersennePrime(2**i-1):
		liz.append(2**i-1)
print liz		
			
