# generating prime numbers according to fermats little theorem

def isPrime(num):
	if (2**num)%num==(2%num):
		return True
	else:
		return False
start=input()
end=input()
liz=[]
for i in range(start,end):
	if isPrime(i) and i!=1:
		liz.append(i)
print liz	 	
	
