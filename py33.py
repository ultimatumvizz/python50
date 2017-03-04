# carmicheal numbers are those numbers which satisfy fermats little theorem but are not prime.
import math
def isPrime(num):
	for i in range(2,int(math.sqrt(num))):
		if num%i==0:
			return False
	return True
def Fermat(num,base):
	if (base**num)%num==(base%num):
		return True
	else:
		return False	
def carmicheal(num):
	if Fermat(num,3) and Fermat(num,5) and not isPrime(num):
		return True
	else:
		return False
start=input()
end=input()
liz=[]
for i in range(start,end):
	if carmicheal(i):
		liz.append(i)
print liz	
